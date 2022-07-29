import os
import sys
from time import sleep

import click
import requests

global nb_total_tests
global nb_test_ran, nb_test_passed, nb_test_failed, nb_test_skipped
global test_final_status
global status_passed, status_failed, status_skipped
global endpoints

status_passed = "🟢"
status_skipped = "🟡"
status_failed = "🔴"


ExitStatus_failure = 1
ExitStatus_success = 0

current_directory = os.path.dirname(os.path.abspath(__file__))


def get_nb_tests(url, header, endpoints, specific_endpoints=[], specific_models=""):
    nb_total_tests = 0
    for path, details in endpoints["paths"].items():
        if specific_endpoints:
            if path in specific_endpoints:
                if specific_models:
                    nb_total_tests += len(specific_models)
                else:
                    nb_total_tests += get_nb_models(url, path, header)
        else:
            nb_total_tests += get_nb_models(url, path, header)

    return nb_total_tests


def get_nb_models(url, path, header):
    response = requests.get(f"{url}{path}", headers=header)
    models = response.json()["models"]
    return len(models)


def request_endpoint(
    url, path, header, params=False, data={}, files=False, max_retry=3
):
    response = type("", (), {})()
    response.status_code = 500
    tries = 1
    while tries <= max_retry and response.status_code != 200:
        if params != False and files != False:
            response = requests.post(
                f"{url}{path}", headers=header, params=params, data=data, files=files
            )
            file = files[next(iter(files))][0]
            if file is None:
                file = "url"
            print(f"|  |       ___ Try : {tries}/{max_retry}    ({file})")
        else:
            response = requests.post(f"{url}{path}", headers=header, params=params)
            print(f"|  |       ___ Try : {tries}/{max_retry}")
        print(f"|  |      |    |_ Response : {response.status_code} ")
        tries += 1
    print(f"|  |      |")

    return response


def perform_test(
    details, url, header, path, skip_when_failed, max_retry=3, specific_models=[]
):
    global nb_test_ran, nb_test_passed, nb_test_failed, nb_test_skipped
    global test_final_status
    global status_passed, status_failed, status_skipped
    global nb_total_tests
    global IS_CI
    global endpoints

    tag = details["get"]["tags"][0]

    if specific_models != []:
        models = specific_models
    else:
        response = requests.get(f"{url}{path}", headers=header)
        models = response.json()["models"]

    for model in models:
        if IS_CI:
            sleep(1)

        input, output, task = details["post"]["tags"][0].split(".")
        status = ""

        if input == "image":
            params = (("model", model),)

            files_to_test = ["test.jpg", "test.png"]
            valid = True

            for file_name in files_to_test:
                file_path = os.path.join(current_directory, file_name)
                files = {"image": (file_name, open(file_path, "rb"))}

                response = request_endpoint(
                    url=url,
                    path=path,
                    header=header,
                    params=params,
                    files=files,
                    max_retry=max_retry,
                )

                if response.status_code != 200:
                    valid = False

            # testing url ref for heavy modality
            files = {
                "image_url": (
                    None,
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1200px-Image_created_with_a_mobile_phone.png",
                ),
            }
            response = request_endpoint(
                url=url,
                path=path,
                header=header,
                params=params,
                files=files,
                max_retry=max_retry,
            )
            if response.status_code != 200:
                valid = False

            if valid:
                nb_test_passed += 1
                status = status_passed
            else:
                nb_test_failed += 1
                status = status_failed
                test_final_status = ExitStatus_failure

        elif input == "audio":
            params = (("model", model),)

            files_to_test = ["test.mp3", "test.wav", "test.m4a"]
            valid = True

            for file_name in files_to_test:
                file_path = os.path.join(current_directory, file_name)
                files = {"audio": (file_name, open(file_path, "rb"))}

                response = request_endpoint(
                    url=url,
                    path=path,
                    header=header,
                    params=params,
                    files=files,
                    max_retry=max_retry,
                )

                if response.status_code != 200:
                    valid = False

            # testing url ref for heavy modality
            files = {
                "audio_url": (None, "https://anshe.org/audio/3Weeks-080715.mp3"),
            }
            response = request_endpoint(
                url=url,
                path=path,
                header=header,
                params=params,
                files=files,
                max_retry=max_retry,
            )
            if response.status_code != 200:
                valid = False

            if valid:
                nb_test_passed += 1
                status = status_passed
            else:
                nb_test_failed += 1
                status = status_failed
                test_final_status = ExitStatus_failure

        elif input == "text":
            params = {"model": model}
            request_body_info = details["post"]["requestBody"]["content"][
                "application/json"
            ]["schema"]
            data = {}
            if "title" in request_body_info:
                data[request_body_info["title"]] = request_body_info["default"]
            else:
                schema = request_body_info["$ref"].split("/")[-1]
                properties = endpoints["components"]["schemas"][schema]["properties"]
                for key, value in properties.items():
                    data[value["title"]] = value["default"]

            response = request_endpoint(
                url=url,
                path=path,
                header=header,
                params=params,
                data=data,
                max_retry=max_retry,
            )

            if response.status_code == 200:
                status = status_passed
                nb_test_passed += 1

            else:
                status = status_failed
                nb_test_failed += 1
                test_final_status = ExitStatus_failure
                if IS_CI:
                    sleep(2)

        nb_test_ran += 1

        progress = round((nb_test_ran / nb_total_tests) * 100, 2)
        print(f"|  |__ {status} {model} ({progress}%)  <{response.status_code}>")
        print(f"|  |")
        if skip_when_failed:
            if status == status_failed:
                sys.exit(status_failed)
    print("|")


def write_github_comment(github_token, github_pull_request, output):
    if github_pull_request != "main":
        print("output:" + output)
        url = f"https://api.github.com/repos/gladiaio/gladia/issues/{github_pull_request}/comments"
        header = {
            "Authorization": f"token {github_token}",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }
        data = '{"body": "' + output.replace("\n", "\\n") + '"}'

        response = requests.post(url, headers=header, data=data)

        return response.status_code
    else:
        return "ok"


@click.command()
@click.option(
    "-u",
    "--url",
    type=str,
    default=f"http://localhost:{os.getenv('API_SERVER_PORT_HTTP', default='8080')}",
    help="URL to test",
)
@click.option(
    "-b",
    "--bearer_token",
    type=str,
    default="",
    help="Bearer token for the secured url (if applicable)",
)
@click.option(
    "-s",
    "--specific_endpoints",
    type=str,
    default="",
    help="CSV separated list of specific endpoints/routes to test format is /input/output/singular_format_task/",
)
@click.option(
    "-m",
    "--specific_models",
    type=str,
    default="",
    help="CSV separated list of specific models to test format is model1,model2",
)
@click.option(
    "-c",
    "--continue_when_failed",
    type=bool,
    is_flag=True,
    default=False,
    help="Continue all other tests even when 1 test failed",
)
@click.option(
    "-a",
    "--after_endpoint",
    type=str,
    default="",
    help="All tests prior to the specified endpoint will be ignored. Specified endpoint is /input/output/singular_format_task/",
)
@click.option(
    "-r",
    "--max_retry",
    type=int,
    default=3,
    help="Number of retry for testing endpoints",
)
@click.option(
    "-g",
    "--github_comment",
    is_flag=True,
    show_default=True,
    default=False,
    help="Write the test result in a GitHub comment",
)
@click.option(
    "-t",
    "--github_token",
    type=str,
    show_default=False,
    default="",
    help="Github Token for the GitHub comment",
)
@click.option(
    "-p",
    "--github_pull_request",
    type=str,
    show_default=False,
    default="",
    help="Github Pull request for the GitHub comment",
)
def main(
    url,
    bearer_token,
    specific_endpoints,
    specific_models,
    continue_when_failed,
    after_endpoint,
    max_retry,
    github_comment,
    github_token,
    github_pull_request,
):

    global endpoints

    skip_when_failed = not continue_when_failed
    if specific_endpoints:
        specific_endpoints = specific_endpoints.split(",")
    else:
        specific_endpoints = []

    if specific_models:
        specific_models = specific_models.split(",")
    else:
        specific_models = []

    header = {"Authorization": "Bearer " + bearer_token}
    response = requests.get(f"{url}/openapi.json", headers=header)
    endpoints = response.json()

    # if the specific endpoint is less
    # then 4 it means it's looking to
    # have a input or input/output mod
    # this should also help to handle
    # missing trailing /
    these_specific_endpoints = []
    for specific_endpoint in specific_endpoints:
        if len(specific_endpoint.split("/")) < 4:
            for endpoint in endpoints["paths"].keys():
                if endpoint.startswith(specific_endpoint):
                    these_specific_endpoints.append(endpoint)

    if these_specific_endpoints != []:
        specific_endpoints = list(dict.fromkeys(these_specific_endpoints))

    print()
    print(f"Testing endpoints")
    print()

    global nb_total_tests, nb_test_ran, nb_test_passed, nb_test_failed, nb_test_skipped
    global test_final_status

    nb_test_skipped = 0
    nb_test_passed = 0
    nb_test_failed = 0
    nb_test_ran = 0
    nb_total_tests = get_nb_tests(
        url, header, endpoints, specific_endpoints, specific_models
    )

    after_endpoint_continue = False
    test_final_status = ExitStatus_success

    for path, details in endpoints["paths"].items():
        print(f"|__ {path}")
        print(f"|  |")
        if specific_endpoints:
            if path in specific_endpoints:
                perform_test(
                    details,
                    url,
                    header,
                    path,
                    skip_when_failed,
                    max_retry,
                    specific_models,
                )

            elif after_endpoint != "":
                if path in after_endpoint:
                    after_endpoint_continue = True

                if after_endpoint_continue:
                    perform_test(
                        details, url, header, path, skip_when_failed, max_retry
                    )
                else:
                    print(f"|  |__ {status_skipped}  <Skipped>")
                    print(f"|")
                    nb_test_skipped += 1

            else:
                print(f"|  |__ {status_skipped}  <Skipped>")
                print(f"|")
                nb_test_skipped += 1

        elif after_endpoint != "":
            if path in after_endpoint:
                after_endpoint_continue = True

            if after_endpoint_continue:
                perform_test(details, url, header, path, skip_when_failed, max_retry)
            else:
                print(f"|  |__ {status_skipped}  <Skipped>")
                print(f"|")
                nb_test_skipped += 1
        else:
            perform_test(details, url, header, path, skip_when_failed, max_retry)

    if test_final_status == ExitStatus_success:
        str_final_status = "Success"
    else:
        str_final_status = "Failure"
    output = f"""
    Final status: {str_final_status}
    Test Passed: {nb_test_passed}/{nb_total_tests} ({round((nb_test_passed / nb_total_tests)*100, 2)}%)
    Test Failed: {nb_test_failed}/{nb_total_tests}  ({round((nb_test_failed / nb_total_tests)*100, 2)}%)
    Test Skipped: {nb_test_skipped}
    """

    print(output)

    if github_comment:
        if github_token == "":
            print("Github token is required to write a comment")
            sys.exit(1)
        if github_pull_request == "":
            print("Github pull request is required to write a comment")
            sys.exit(1)
        write_github_comment(github_token, github_pull_request, output)

    sys.exit(test_final_status)


if __name__ == "__main__":
    global IS_CI
    IS_CI = os.getenv("IS_CI", "False").lower() in ("true", "1", "t", "y", "yes")
    main()
