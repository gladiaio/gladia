# Custom environments

## How do custom environments are built

Each task/model can have an `env.yaml` file describing the custom environment to use.

Notes :
- If both the task and the model have an `env.yaml` file, the model custom environment will take precedence for its own specific model.\
- If a model does not have an `env.yaml` file but the task do, the model will be launched using the task's `env.yaml` file.

An `env.yaml` file is described as follow:
```yaml
inherit:
  - templates-to-inherit-from

dependencies:
  - conda-forge-dependencies
  - pip:
    - pip-dependencies
```

A custom environment can inherit from templates (see [this folder](src/venv-builder/envs)).\
Templates contain multiple package related to either a modality (i.e image) or a package (i.e pytorch). Templates are useful to build custom environment without having to list each package every time.

Note : a custom environment must have either a conda-forge dependency, a pip dependency or a inherit value.

## Usage

Before building any custom environment, be sure to be in the `venv-builder` folder.

Usages:
* To build every custom envs : `python create_custom_envs.py`
* To build a specific custom env : `python create_custom_envs.py --name PATH_TO_A_TASK` \
(You can specify mutliple paths using multiple times the `--name` flag and can specify a path to a specific model or `env.yaml` instead of task)