#!/bin/bash

# example usage: ./run.sh autoencoders/one_hot_vectors.py

# NOTE: You need Docker to run this script.

if [[ $# -eq 0 ]] ; then
    echo USAGE: $0 '<path_to_script>'
    exit 0
fi

IMAGE_NAME="neuralfun"

if ! [[ `docker images | grep ${IMAGE_NAME}` ]]; then
   echo No image found. Building...
   docker build -t ${IMAGE_NAME} .
fi

docker run -v `pwd`:/opt -w /opt -t ${IMAGE_NAME} $*
