import os
import pathlib
import shutil
import sys

dir_ignore = ["__pycache__"]
root_path = os.getcwd()


def manage_metadata_files(argv):

    delete = True if "delete" in argv else False

    model_paths = []
    task_paths = []

    # /apis/
    path = os.path.join(root_path, "apis")
    input_dir_list = os.listdir(path)
    # /apis/<input>/
    for input_dir in input_dir_list:
        input_dir_path = os.path.join(path, input_dir)
        if os.path.isdir(input_dir_path) and input_dir not in dir_ignore:
            output_dir_list = os.listdir(input_dir_path)
            # /apis/<input>/<output>/
            for output_dir in output_dir_list:
                output_dir_path = os.path.join(input_dir_path, output_dir)
                if os.path.isdir(output_dir_path) and output_dir not in dir_ignore:
                    task_dir_list = os.listdir(output_dir_path)
                    # /apis/<input>/<output>/<task>/
                    for task_dir in task_dir_list:
                        task_dir_path = os.path.join(output_dir_path, task_dir)
                        if os.path.isdir(task_dir_path) and task_dir not in dir_ignore:
                            model_dir_list = os.listdir(task_dir_path)
                            if model_dir_list != [".empty"]:
                                task_paths.append(task_dir_path)
                            # /apis/<input>/<output>/<task>/<model>/
                            for model in model_dir_list:
                                model_path = os.path.join(task_dir_path, model)
                                if (
                                    os.path.isdir(model_path)
                                    and model not in dir_ignore
                                ):
                                    model_paths.append(model_path)

    source_task_metadata_path = os.path.join(
        root_path, "apis/.metadata_task_template.json"
    )
    source_model_metadata_path = os.path.join(
        root_path, "apis/.metadata_model_template.json"
    )
    destination_file_name = ".metadata.json"

    # Create or delete task metadata files
    for task_path in task_paths:
        destination_file = os.path.join(task_path, destination_file_name)
        if not delete:
            shutil.copy(source_task_metadata_path, destination_file)
        else:
            to_delete_file_path = os.path.join(task_path, destination_file_name)
            if pathlib.Path(to_delete_file_path).exists():
                os.remove(to_delete_file_path)

    # Create or delete modele metadata files
    for model_path in model_paths:
        destination_file = os.path.join(model_path, destination_file_name)
        if not delete:
            shutil.copy(source_model_metadata_path, destination_file)
        else:
            to_delete_file_path = os.path.join(model_path, destination_file_name)
            if pathlib.Path(to_delete_file_path).exists():
                os.remove(to_delete_file_path)


if __name__ == "__main__":
    manage_metadata_files(sys.argv)
