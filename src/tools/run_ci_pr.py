import json
import sys

import click
import requests


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def has_only_pr_with_prefix(response, prefix_to_check, verbose):
    only_prs_with_prefix = True
    # check all associated PR with a commit
    # if there is at least 1 PR without the prefix in the title
    # change the only_prs_with_prefix to False
    data = response.json()
    if data["total_count"] > 0:
        if verbose:
            print(f"{bcolors.OKGREEN}Found {data['total_count']} PRs{bcolors.ENDC}")

        # for each PR check if the PR title doesn't contains WIP in the title
        # change the skip_build to False
        for pr in data["items"]:
            if verbose:
                print(
                    f"{bcolors.OKGREEN}Checking PR {pr['number']}: {pr['title']} {bcolors.ENDC}"
                )

            # if the PR title doesn't contains the prefix
            # in the first characters of the title
            if not pr["title"].upper().startswith(prefix_to_check.upper()) and not pr[
                "title"
            ].upper().startswith(f"({prefix_to_check.upper()})"):
                only_prs_with_prefix = False
                break
        if verbose:
            if only_prs_with_prefix:
                print(
                    f"{bcolors.FAIL}Only PRs with prefix {prefix_to_check} found{bcolors.ENDC}"
                )
            else:
                print(
                    f"{bcolors.OKGREEN}PRs without prefix {prefix_to_check} also found{bcolors.ENDC}"
                )

    else:
        print(f"{bcolors.FAIL}No PR found for commit{bcolors.ENDC}")

    return only_prs_with_prefix


# using an access token
@click.command()
@click.option("--commit_short", default="", required=True, help="Short Sha of commit.")
@click.option(
    "--repo",
    default="gladiaio/gladia",
    show_default=True,
    required=False,
    help="Repo to scan",
)
@click.option("--gh_token", default="", required=True, help="Github Token")
@click.option(
    "--prefix_to_check",
    default="WIP",
    show_default=True,
    required=True,
    help="PR prefix to check e.g.",
)
@click.option(
    "--break_when_only_prefix",
    is_flag=True,
    show_default=True,
    default=False,
    help="Exit 1 when all PR have the prefix",
)
@click.option(
    "--break_if_no_pr",
    is_flag=True,
    show_default=True,
    default=False,
    help="Exit 1 when all PR have the prefix",
)
@click.option(
    "--return_pr",
    is_flag=True,
    show_default=False,
    default=False,
    help="Return the list of PR associated to the commit",
)
@click.option(
    "--pr_nb_only",
    is_flag=True,
    show_default=False,
    default=False,
    help="Return PR ids to the commit",
)
@click.option(
    "--first_pr_only",
    is_flag=True,
    show_default=False,
    default=False,
    help="Return PR the first PR where the commit appears",
)
@click.option(
    "--deploy_message",
    is_flag=True,
    show_default=False,
    default=False,
    help="Return the deploy message associated to the PR",
)
@click.option(
    "--verbose", is_flag=True, show_default=False, default=False, help="Verbose output"
)
def commit_should_run(
    commit_short="",
    repo="gladiaio/gladia",
    gh_token="",
    prefix_to_check="WIP",
    break_when_only_prefix=False,
    break_if_no_pr=False,
    return_pr=False,
    pr_nb_only=False,
    first_pr_only=False,
    deploy_message=False,
    verbose=False,
):
    if deploy_message:
        pr_nb_only = True
        return_pr = True
        verbose = False

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {gh_token}",
    }

    query = f"https://api.github.com/search/issues?q={commit_short}+repo:{repo}+type:pr"
    response = requests.get(query, headers=headers)

    this_pr = dict()

    if response.status_code == 200:
        # check if there is a PR associated with the commit
        if response.json()["total_count"] == 0:
            if break_if_no_pr:
                if verbose:
                    print(
                        f"{bcolors.FAIL}No PR found with prefix {prefix_to_check} for commit{bcolors.ENDC}"
                    )
                sys.exit(1)

        has_honly_prefix = has_only_pr_with_prefix(
            response, prefix_to_check=prefix_to_check, verbose=verbose
        )

        if return_pr or deploy_message:
            data = response.json()
            prs = []
            if data["total_count"] > 0:
                for pr in data["items"]:
                    if pr_nb_only:
                        prs.append(int(pr["number"]))
                        this_pr = pr

                    else:
                        prs.append(f'[{pr["number"]}] {pr["title"]}')
            if not deploy_message:
                if first_pr_only:
                    print(min(prs))
                else:
                    print(" | ".join(map(str, prs)))

            if deploy_message:
                if this_pr:
                    pr_url = this_pr["pull_request"]["html_url"]
                    title = this_pr["title"]
                    number = this_pr["number"]
                    user = this_pr["user"]["login"]
                    timeline_url = this_pr["timeline_url"]

                    # get the timeline of the PR
                    # as json to dict using requests
                    timeline_response = requests.get(timeline_url, headers=headers)
                    timeline_data = timeline_response.json()

                    # concatenate the deploy message
                    # extraction all the commit short sha and messages
                    deploy_message = f"[{number}]{title} by {user} - {pr_url}\n"
                    for item in timeline_data:
                        # if user is not github
                        # and the event is a commit not a merge branch 'main'
                        # which means an update

                        if item["event"] == "committed":
                            if item["committer"]["name"] != "GitHub":
                                if (
                                    item["message"].startswith("feat")
                                    or item["message"].startswith("add")
                                    or item["message"].startswith("(feat)")
                                ):
                                    deploy_message += "✨"
                                elif item["message"].startswith("fix") or item[
                                    "message"
                                ].startswith("(fix)"):
                                    deploy_message += "🐛"
                                elif item["message"].startswith("docs") or item[
                                    "message"
                                ].startswith("(docs)"):
                                    deploy_message += "📚"
                                elif (
                                    item["message"].startswith("style")
                                    or item["message"].startswith("format")
                                    or item["message"].startswith("(style)")
                                ):
                                    deploy_message += "💄"
                                elif item["message"].startswith("refactor") or item[
                                    "message"
                                ].startswith("(refactor)"):
                                    deploy_message += "🔧"
                                elif item["message"].startswith("test") or item[
                                    "message"
                                ].startswith("(test)"):
                                    deploy_message += "🔬"
                                elif item["message"].startswith("chore") or item[
                                    "message"
                                ].startswith("(chore)"):
                                    deploy_message += "📝"
                                elif item["message"].startswith("ci") or item[
                                    "message"
                                ].startswith("(ci)"):
                                    deploy_message += "🚧"
                                elif item["message"].startswith("revert") or item[
                                    "message"
                                ].startswith("(revert)"):
                                    deploy_message += "🔙"
                                elif (
                                    item["message"].startswith("perf")
                                    or item["message"].startswith("improve")
                                    or item["message"].startswith("(perf)")
                                ):
                                    deploy_message += "🏃"
                                elif item["message"].startswith("build") or item[
                                    "message"
                                ].startswith("(build)"):
                                    deploy_message += "🚧"
                                elif item["message"].startswith("release") or item[
                                    "message"
                                ].startswith("(release)"):
                                    deploy_message += "🏷"
                                elif item["message"].startswith(
                                    "[pre-commit.ci]"
                                ) or item["message"].startswith("Merge branch"):
                                    pass
                                else:
                                    deploy_message += "💬"

                                deploy_message += f"({item['sha'][:7]}) {item['message']} ({item['committer']['name']})\n"

                    # print the deploy message
                    print(deploy_message)

                else:
                    print("No PR found")

        else:
            if break_when_only_prefix:
                sys.exit(1 if has_honly_prefix else 0)
            else:
                print(has_honly_prefix)
    else:
        print(
            f"{bcolors.FAIL}Error {response.status_code} {response.reason} {bcolors.ENDC}"
        )


if __name__ == "__main__":
    commit_should_run()
