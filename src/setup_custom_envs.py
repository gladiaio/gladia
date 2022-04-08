#!/usr/bin/env python3
import os
import yaml
import click
from multiprocessing.pool import ThreadPool as Pool
import multiprocessing

# Make the VENV is built and stored nearby the API folder
# https://stackoverflow.com/questions/57919110/how-to-set-pipenv-venv-in-project-on-per-project-basis
# the purpose is to make sure that the API_UTILS catches the existence of the venv when running the inference
os.environ["PIPENV_VENV_IN_PROJECT"] = os.getenv('PIPENV_VENV_IN_PROJECT', 'enabled')

@click.command()
@click.option('-r', '--rootdir', type=str, default='apis', help="Build env recursively from the provided directory path")
@click.option('-p', '--poolsize', type=int, default=0, help="Parallelness if set to 0 will use all threads")
@click.option('-s', '--simlink', type=bool, default=False, help="Will simlink gladia-api-utils from the local version of gladia-api-utils")
@click.option('-f', '--force', type=bool, default=False, help="Force rebuilding venv")
def main(rootdir, poolsize, simlink, force):
    print(force)
    print(simlink)
    if poolsize == 0:
        pool = Pool(multiprocessing.cpu_count())
    else:
        pool = Pool(poolsize)

    for dirName, subdirList, fileList in os.walk(rootdir):
        pool.apply_async(build_env, (dirName, subdirList, fileList, simlink, force, ))

    pool.close()
    pool.join()


def build_env(dirName, subdirList, fileList, simlink, force):
    if 'env.yaml' in fileList:
        print(f"Found env.yaml in {dirName}")
        with open(os.path.join(dirName, 'env.yaml'), 'r') as stream:
            try:
                env_yaml = yaml.safe_load(stream)
                print(f"Loaded env.yaml in {dirName}")
            except yaml.YAMLError as exc:
                print(exc)

            build = True
            if os.path.exists(os.path.join(dirName, '.venv')):
                print("existing .venv found")
                if force == True:
                    try:
                        os.system(f"cd {dirName} && rm -rf .venv Pipfile")
                    except:
                        print("Could not remove .venv and Pipfile")
                        build = False
                else:
                    build = False
            
            if build == True:
                packages_to_install = ' '.join(env_yaml['packages'])

                if simlink:
                    packages_to_install += ' gladia-api-utils'
            
                os.system(f"cd {dirName} && echo Y | pipenv --python {env_yaml['python']['version']}")
                os.system(f"cd {dirName} && pipenv run pip install {packages_to_install}")

                if simlink:
                    os.system(f"ln -s /opt/conda/lib/python3.7/site-packages/gladia_api_utils {dirName}/.venv/lib/python3.7/site-packages/gladia_api_utils")


if __name__ == '__main__':
    main()
