import os
import click
from multiprocessing.pool import ThreadPool as Pool
import multiprocessing

from utils import \
    install_packages_in_pipenv_from_file, \
    install_packages_in_pipenv_from_string

from utils import \
    get_packages, \
    get_env_conf

from utils import \
    build_env_from_modality, \
    boot_pipenv

from utils import \
    simlink_if_source_exists, \
    simlink_lib_so_files, \
    simlink_bin_files, \
    simlink_site_packages

from utils import \
    mkdir

from utils import \
    clean_env, \
    clean_dir, \
    clean_file, \
    clean_dir_without_parent


# Make the VENV is built and stored nearby the API folder
# https://stackoverflow.com/questions/57919110/how-to-set-pipenv-venv-in-project-on-per-project-basis
# the purpose is to make sure that the API_UTILS catches the existence of the venv when running the inference
os.environ["PIPENV_VENV_IN_PROJECT"] = os.getenv('PIPENV_VENV_IN_PROJECT', 'enabled')
os.environ["PIPENV_VENV_TMP_BASE_PATH"] = os.getenv('PIPENV_VENV_TMP_BASE_PATH', '/tmp/gladia/venv/')
os.environ["PIPENV_VENV_DEFAULT_PY_VERSION"] = os.getenv('PIPENV_VENV_DEFAULT_PY_VERSION', '3.7')

os.environ["PIPENV_VENV_DEFAULT_COMMON_PACKAGES_TXT"] = os.getenv('PIPENV_VENV_DEFAULT_COMMON_PACKAGES_TXT', os.path.join(os.getcwd(), 'default_common_packages.txt'))
os.environ["PIPENV_VENV_DEFAULT_IMAGE_PACKAGES_TXT"] = os.getenv('PIPENV_VENV_DEFAULT_IMAGE_PACKAGES_TXT', os.path.join(os.getcwd(), 'default_image_packages.txt'))
os.environ["PIPENV_VENV_DEFAULT_SOUND_PACKAGES_TXT"] = os.getenv('PIPENV_VENV_DEFAULT_SOUND_PACKAGES_TXT', os.path.join(os.getcwd(), 'default_sound_packages.txt'))
os.environ["PIPENV_VENV_DEFAULT_TEXT_PACKAGES_TXT"] = os.getenv('PIPENV_VENV_DEFAULT_TEXT_PACKAGES_TXT', os.path.join(os.getcwd(), 'default_text_packages.txt'))
os.environ["PIPENV_VENV_DEFAULT_VIDEO_PACKAGES_TXT"] = os.getenv('PIPENV_VENV_DEFAULT_VIDEO_PACKAGES_TXT', os.path.join(os.getcwd(), 'default_video_packages.txt'))


@click.command()
@click.option('-r', '--rootdir', type=str, default=f'{os.getenv("PATH_TO_GLADIA_SRC")}/apis/', help="Build env recursively from the provided directory path")
@click.option('-p', '--poolsize', type=int, default=0, help="Parallelness if set to 0 will use all threads")
@click.option('-s', '--simlink', is_flag=True, type=bool, default=False, help="Will simlink gladia-api-utils from the local version of gladia-api-utils")
@click.option('-c', '--compact_mode', is_flag=True, type=bool, default=False, help="Enable compact mode simlinking the default packages")
@click.option('-f', '--force', is_flag=True, type=bool, default=False, help="Force rebuilding venv")
@click.option('-b', '--base', is_flag=True, type=bool, default=False, help="Build the base for custom env")
@click.option('-t', '--trash_cache', is_flag=True, type=bool, default=False, help="Trash the pipenv cache")
@click.option('-l', '--local_venv_trash_cache', is_flag=True, type=bool, default=False, help="Trash the pipenv cache on cust venv")
@click.option('-d', '--teardown_common_env', is_flag=True, type=bool, default=False, help="Tear common venv")
@click.option('-B', '--build_all_env', is_flag=True, type=bool, default=False, help="Build all cust venv")
@click.option('-x', '--clean_all_venv', is_flag=True, type=bool, default=False, help="Clean all cust venv")
def main(rootdir, poolsize, simlink, force, base, compact_mode, trash_cache, local_venv_trash_cache, clean_all_venv, teardown_common_env, build_all_env):

    rootdir = os.path.abspath(rootdir)

    global envs_base_dict
    global default_python_version

    default_python_version = str(os.environ["PIPENV_VENV_DEFAULT_PY_VERSION"])
    envs_base_dict = dict()

    envs = ['common', 'image', 'sound', 'text', 'video']
    for env in envs:
        envs_base_dict[env] = {
            'path' : os.path.join(os.environ['PIPENV_VENV_TMP_BASE_PATH'], env),
            'packages_file' : os.environ[f'PIPENV_VENV_DEFAULT_{env.upper()}_PACKAGES_TXT']
        }

    # build template enviroments
    # This can only work on a non-parallel build
    # as there is an order of execution
    if base:

        # order of execution matters
        # we want common first as it's the most generic
        # then we need image, sound, and text that are all
        # potentially used for video
        
        previous_envs = list()
        envs = ["common", "image", "sound", "text", "video"]
        for env in envs:
            print("---------------")
            print(f"Overriding common base for base {env} venv")
            print("---------------")

            print(f"Preparing {env} env")
            mkdir(envs_base_dict[env]['path'])
            
            print(f"Cleaning {env} env")
            clean_dir_without_parent(envs_base_dict[env]['path'])
            
            print(f"Booting {env} env")
            boot_pipenv(envs_base_dict[env]['path'], default_python_version)
            

            print("Installing common packages")
            install_packages_in_pipenv_from_file(envs_base_dict[env]['path'], envs_base_dict['common']['packages_file'])

            print(f"Installing {env} packages")
            # install packages on top of common
            install_packages_in_pipenv_from_file(envs_base_dict[env]['path'], envs_base_dict[env]['packages_file'])

            for previous_env in previous_envs:
                print(f"Stacking {previous_env} packages on {env}")
                
                source_path = os.path.join(envs_base_dict[previous_env]['path'], '.venv')
                target_path = os.path.join(envs_base_dict[env]['path'], '.venv')

                print("Simlinking common env")
                simlink_lib_so_files(source_path, target_path)
                simlink_bin_files(source_path, target_path)
                simlink_site_packages(source_path, target_path, default_python_version)
            
            previous_envs.append(env)


    # define parallelization strategy
    if poolsize == 0:
        pool = Pool(multiprocessing.cpu_count())
    else:
        pool = Pool(poolsize)
    

    print("---------------")
    print(f"Scanning {rootdir}")
    print("---------------")
    
    # Crawl all endpoints and modalities
    # to build env if necessary
    for dirName, subdirList, fileList in os.walk(rootdir):
            
        # avoid traversing the cache and the exisiting venvs
        if (".venv" not in dirName) and ("__pycache__" not in dirName):
            if clean_all_venv:
                if poolsize == 1:
                    # easier debugging
                    # multi-threading tends to hide errors
                    clean_env(dirName, subdirList, fileList)

                else:
                    pool.apply_async(clean_env, (dirName, subdirList, fileList, ))
        
            # Building env will autoomagically remove
            # existing venvs if force is set
            if build_all_env:
                if poolsize == 1:
                    # easier debugging
                    # multi-threading tends to hide errors
                    build_env(dirName, fileList, simlink, force, compact_mode, local_venv_trash_cache)
                else:   
                    pool.apply_async(build_env, (dirName, fileList, simlink, force, compact_mode, local_venv_trash_cache, ))

    pool.close()
    pool.join()

    
    if teardown_common_env:
        print("---------------")
        print("cleaning common venv")
        print("---------------")
        clean_dir(os.path.join(os.environ['PIPENV_VENV_TMP_BASE_PATH'], "common"))

    if trash_cache:
        print("---------------")
        print("cleaning general cache")
        print("---------------")
        clean_dir("/root/.cache/*")


def build_env(dirName, fileList, simlink, force, compact_mode, local_venv_trash_cache):
    # if env.yaml exist => will trigger a custom env could be
    # the default one from the modality
    if 'env.yaml' in fileList:
        print("---------------")
        print(f"Building {dirName}")
        print("---------------")

        # check the custom env requirements
        with open(os.path.join(dirName, 'env.yaml'), 'r') as stream:
            print("---------------")
            print("Guessing the input modality to apply the right base env")
            
            splitted_path = dirName.split("/")
            input_modality = ""
            for item in splitted_path:
                if item in ["image", "audio", "video", "text"]:
                    input_modality = item
                    break
            
            print(f"Found input modality to be : {input_modality}")
            print("---------------")

            env_yaml = get_env_conf(stream)
            python_version = str(env_yaml['python']['version'])

            # build is a flag
            # that will lead to the build of a 

            # has_custom_packages is a flag to know if
            # you have additionnal package vs the default one from
            # the modality / the env template            
            has_custom_packages, extra_packages_to_install = get_packages(env_yaml)

            custom_env_directory = os.path.join(dirName, '.venv')
            modality_base_env_directory = os.path.join(os.environ['PIPENV_VENV_TMP_BASE_PATH'], input_modality)
            
            # if a custom env seems to be already there
            # depending on the --force arg will trigger a rebuild
            # if no custom env there or forced:
            # if the env has no packages => use the default env of the modality
            # this is checked using the has_custom_packages
            # else build a custom env for the endpoint and try to simlink binaries and libs
            # /!\ linking binaries is complicated as some Sheebangs are happened in general to them
            # binding explicitely the bins to their original location
            
            if os.path.exists(custom_env_directory):
                if force:
                    print("---------------")
                    print("Using Force mode and remove .venv and Pipfile")
                    print("---------------")

                    # when forcing on existing we delete the venv by
                    # removing the .venv and Pipfile
                    # then if has no custom packages we use the 
                    # default modality env
                    # else we build a custom env stacking the 
                    # common + modality + custom
                    # this what build_env_from_modality is doing
                    try:
                        clean_dir(os.path.join(dirName, '.venv'))
                        clean_dir(os.path.join(dirName, '__pycache__'))
                        clean_file(os.path.join(dirName, 'Pipfile'))

                        build_env_from_modality(dirName, input_modality, has_custom_packages, extra_packages_to_install, python_version, envs_base_dict)

                    except Exception as e: 
                        print("---------------")
                        print("Could not remove .venv and Pipfile")
                        print(str(e))
                        print("---------------")
            
            # if no .venv build it as you have a env.yaml
            else:

                # if custom env needed (because the the env.yaml is there)
                # if no packages => use the default env of the modality
                # we can check the has_custom_packages flag for that purpose
                
                # else build a custom env for the endpoint and try to simlink binaries and libs
                try:
                    print("---------------")
                    print(f"Applying {input_modality} base venv")
                    print("---------------")

                    # if no custom packages => use the default env of the modality
                    # else use build and stack env
                    # this what build_env_from_modality is doing
                    build_env_from_modality(dirName, input_modality, has_custom_packages, extra_packages_to_install, python_version, envs_base_dict)
               
                except Exception as e: 
                    print("---------------")
                    print("Failed starting creation of custom env")
                    print(str(e))
                    print("---------------")
                    
            
            if compact_mode:
                print("---------------")
                print(f"Running in compact mode")
                print("---------------")

                if default_python_version == python_version:
                    
                    print("---------------")
                    print(f"Applying {input_modality} packages simlinks to custom env")
                    print("---------------")

                    # crawl all files in lib excluding folders
                    # and link them is source exists
                    # starting from common then
                    # continue to modality env
                    # skip else

                    source_path = os.path.join(envs_base_dict["common"]['path'], '.venv')
                    target_path = os.path.join(dirName, '.venv')
                
                    # simlinking to common before modality
                    simlink_lib_so_files(source_path, target_path)
                    simlink_bin_files(source_path, target_path)
                    simlink_site_packages(source_path, target_path, python_version)

                    source_path = os.path.join(envs_base_dict[input_modality]['path'], '.venv')
                    # simlinking to modality
                    simlink_lib_so_files(source_path, target_path)
                    simlink_bin_files(source_path, target_path)
                    simlink_site_packages(source_path, target_path, python_version)
            
            if simlink:
                print("---------------")
                print(f"Applying Simlink of API UTILS to {dirName}/.venv/lib/python{os.environ['PIPENV_VENV_DEFAULT_PY_VERSION']}/site-packages/gladia_api_utils")
                print("---------------")
                
                gladia_utils_source_path = os.path.join('/opt/conda/lib/python' + default_python_version, 'site-packages', 'gladia_api_utils')
                gladia_utils_target_path = os.path.join(dirName, '.venv', 'lib', 'python' + python_version, 'site-packages', 'gladia_api_utils')
                simlink_if_source_exists(gladia_utils_source_path, gladia_utils_target_path)
            else:
                install_packages_in_pipenv_from_string(dirName, 'gladia_api_utils')
            
            if local_venv_trash_cache:
                print("---------------")
                print("cleaning local venv")
                print("---------------")
                
                #clean_useless_prod_packages(dirName)

if __name__ == '__main__':
    main()
