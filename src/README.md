# `./run_server_prod.sh` 

This script start the Gladia server. It does mainly three things :

* Setup some environment variables
* Start the [triton server](https://developer.nvidia.com/nvidia-triton-inference-server) using [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html),
* Start the [FASTAPI web server](https://www.uvicorn.org/) using the `app` object instanciated in `main.py` (see [here](https://github.com/gladiaio/gladia/blob/a832381dfa79ed7974fed090fd549fd7abe2c9ee/src/main.py#L199)).

# `main.py`

Apart from performing some chore tasks, `main.py` will walk through the `gladia/src/apis/` directory and look for all the routes to be added to the FASTAPI router object. 

## How will it do it ? 

While walking through the `gladia/src/apis/`, when it will find the `router` object in `gladia/src/apis/{audio,image,text,video}/{audio,image,text,video}/*.py`, then it will attach it to the `app` object from `main.py`. 

Moreover, while importing (in the python sense of the word) those `router` objects, the `TaskRouter` object is instanciated. During the instanciation of `TaskRouter` for each task described in `gladia/src/apis/{audio,image,text,video}/{audio,image,text,video}/*.py`, this is where we bind the logic of the `GET`/`POST` methods to the routes of the task. 

The implementation of `TaskRouter` is in `gladia/src/api_utils/gladia_api_utils/submodules.py`. See :
 
* [here](https://github.com/gladiaio/gladia/blob/a832381dfa79ed7974fed090fd549fd7abe2c9ee/src/api_utils/gladia_api_utils/submodules.py#L235) for the decorated function for the `GET` method
* [here](https://github.com/gladiaio/gladia/blob/a832381dfa79ed7974fed090fd549fd7abe2c9ee/src/api_utils/gladia_api_utils/submodules.py#L264) for the decorated function for the `POST` method

