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

