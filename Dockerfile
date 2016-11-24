FROM ubuntu:16.04

ENV TF_BINARY_URL https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0-cp35-cp35m-linux_x86_64.whl

RUN apt-get update && apt-get install -y \
         python3.5 \
         python3.5-dev \
         python3-numpy \
         python3-scipy \
         python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade ${TF_BINARY_URL}

ENTRYPOINT ["/usr/bin/python3.5"]
