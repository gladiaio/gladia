# Prerequisites

This page makes very few assumptions : 

- the reader has (quasi) no knowledge of how Docker is working
- the developer has a ssh access to a hosting server with GPU capabilities

# Objectives

The objective is for the new developer to be in full control while performing the following first steps :

1. To be able to build and run your own image based on the repository sources
2. Make a first API call to your own newly running container
3. Run the test suite within the newly running container

It is the really first deterministic steps to use Gladia APIs for developer purposes. 

Once this is done, the next steps would be to follow instructions in the repository [README.md](https://github.com/gladiaio/gladia) that provides some useful docker helper files that thankfully abstract some of the details presented here. See especially 

- The [Running the dev environment](../README.md#running-the-dev-environement) section and its [docker-compose.dev.yaml](./docker-compose.dev.yaml)
- The [Run the production environment](../README.md#running-the-production-environement) section and its [docker-compose.prod.yaml](./docker-compose.prod.yaml)
- And the shared [docker-compose.yaml](./docker-compose.yaml)

# Build and run your own image

## Build 

Please see the [Claap video](https://app.claap.io/gladia/howto101-build-the-image-from-the-source-c-IPbrCarAMH-qixm_orQ84ZT).

Provided that you cloned the repo, build your own Docker image. We are giving it a memorable user defined name ( `oboulant/mamba` ) in order to retrieve it later on

```bash
> git clone https://github.com/gladiaio/gladia.git
> cd gladia/src
> docker build -t oboulant/mamba -f gpu.Dockerfile .
```

The `docker build` command may take some time to run since it is building the complete image. Once the it returns, you can check that the image is properly built

```bash
> docker images
```
![List docker images](../images/Screenshot%202022-06-28%20at%2010.58.54.png "List docker images")

## Start a container by running your own image

Please see the [Claap video](https://app.claap.io/gladia/howto101-start-a-container-using-your-own-image-c-IPbrCarAMH-F_dxT_URkA7L).

```bash
> docker run -it --gpus all -e CUDA_VISIBLE_DEVICES=0 --shm-size 8g -p 8080:8080 -v $PWD:/app oboulant/mamba /bin/bash
```

Few comments :

* `-it`  tells docker to start the container in interactive mode
* `--gpus all` make docker being able to see all gpus
* `-e CUDA_VISIBLE_DEVICES=<GPU_ID>` Enable the designated GPU to be used for the docker application. Without this the application will assume all GPUs can be provisioned. You can list the available GPUs using the command
* `--shm-size 8g` Increase shared memory to 8 gigabits in order to process some models
* `-p 8080:8080` Publish the 8080 port in order to access it from your navigator if necessary

```bash
> nvidia-smi
```

* `-v $PWD:/app` tells docker to mount a volume on the container (more on this later on)
* `oboulant/mamba` tells docker which `REPOSITORY`  image to use
* `/bin/bash` tells docker to start a bash console

## Start the Gladia server from within your own running container

The above command will directly open a bash session for you on the newly created container. Within the bash session of your newly created container, you can start Gladia server by running :

```bash
> ./run_server_prod.sh
```

Back to the `-v $PWD:/app`. Mounting a volume means that all `gladia/src` folder content from your hosting server is “mounted”/mapped dynamically within the container under the `/app` directory. Doing so, prevents us to have to restart (or even worst rebuild) each time we modify something in our `gladia/src/` directory from the hosting server. 

Let say you modified something in the `gladia/src/`, then depending on which part of the code you modified :

* Either you do not have anything to do in order to take those modifications into account,
* Or,
    1. You only have to stop the Gladia Server within the container (just `ctrl + C` in the terminal where you started your container)
    2. Restart `./run_server_prod.sh` to take into account your modifications

# Make our first API call to your running container

Please see the [Claap video](https://app.claap.io/gladia/howto101-make-your-very-first-api-call-to-your-own-gladia-container-c-IPbrCarAMH-DNGgVxNGD1yO). 

## Connect to your own container

Open a new terminal session on the remote server. List all running containers in order to see if the container we just launched is indeed running.

```bash
> docker ps
```
![List docker containers](../images/Screenshot%202022-06-28%20at%2011.08.50.png "List docker containers")

We will connect to our own container using the corresponding CONTAINER ID . The `/bin/bash` option just tells docker to open a bash session once we connect to the container.

```bash
> docker exec -it 522b5c0c3a9c /bin/bash
```

You are now logged into the container with a bash session. 

## Make your first API call

For the sake of example, we just perform a call to the Gladia API that computes the similarity between two sentences. It returns a string containing the similarity score. 

```bash 
> curl -X 'POST'  'http://localhost:8080/text/text/similarity/?sentence_1=I%20like%20Python%20because%20I%20can%20build%20AI%20applications&sentence_2=Second%20sentence%20to%20compare%20to&model=all-MiniLM-L6-v2' -H 'accept: application/json' -d ''
```
![First API call from the clien side](../images/Screenshot%202022-06-28%20at%2013.04.54.png "Fist API call from the clien side")

If you go back to the terminal where you started your container, you should see in the terminal the successful incoming call ⤵️
![First API call from the server side](../images/Screenshot%202022-06-28%20at%2013.33.10.png "Fist API call from the server side")

## How to know the specific command line ? 

You can find all available Gladia APIs on the [Gladia API Swagger](http://aipi.gladia.io/docs). Here, you can browse on all APIs. Most of the time

- The GET request lists all available models for the given task
- The POST request allows you to actually call a given model with the provided inputs

Using the Gladia API Swagger, you can try it out. Once you Execute the POST request within the Gladia API Swagger, it will output the curl command to call you chosen API with the given model and the provided inputs. 

![AIPI Swagger](../images/Screenshot%202022-06-28%20at%2013.14.20.png "AIPI Swagger")

![AIPI Swagger curl command](../images/Screenshot%202022-06-28%20at%2013.18.38.png "AIPI Swagger curl command")

Once you have the `curl` command, you will only have to replace `http://aipi.gladia.io` by `http://localhost:8080` in the Request URL so that the call will target your own running container on your hosting server rather than Gladia’s production server.

# Run the tests on your running container

## Connect to your own container

Please refer to the [previous section](#connect-to-your-own-container) in order to open a new terminal on your running container. 

## Run the tests

Please see the [Clapp video](https://app.claap.io/gladia/howto101-run-the-tests-suite-c-IPbrCarAMH-R2ntOpAFdPA9).

```bash
> cd unit-test
> python test.py -c
# or
> python test.py --continue_when_failed
```

The `--continue_when_failed` option (or `-c` in short version) prevents the testing framework to stop whenever a single test fails. It tells it to “continue” in such cases.

# Bonus : Make your very fisrt debug `print` 

Please see the [Claap video](https://app.claap.io/gladia/howto101-make-your-very-first-debug-print-c-IPbrCarAMH-aYRK_Jy3nhrX).
