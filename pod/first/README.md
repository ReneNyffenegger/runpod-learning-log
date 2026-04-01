# First runpod pod

## Files

### Dockerfile

I tried start the [`Dockerfile`](Dockerfile) with `FROM alpine:latest`.
Because Alpine Linux uses the musl C library by default, I was unable to run `nvidia-smi` which
are compiled against glibc.\
Therefore, I changed to [`greyfoxit/alpine-glibc`](https://github.com/greyfoxit/alpine-glibc) which uses the GNU C library.
[`frolvlad/alpine-glibc`](https://hub.docker.com/r/frolvlad/alpine-glibc/) would have been another alternative.

### go.sh

[`go.sh`](go.sh) is the script that calls most the scripts below in the correct order to create docker image,
template and pod.

### docker-build

[`docker-build`](docker-build) builds a docker image and pushes it to [docker hub](https://hub.docker.com/r/renenyffenegger/runpod-minimal-pod).

### create-template

[`create-template`](create-template) creates the template which is used to create the pod.

### create-pod

[`create-pod`](create-pod) uses [`create-from-json-body`](../../API/pods/create-from-json-body) to create a pod.

### clean-up

[`clean-up`](clean-up) removes the pod and the template.

The script must be sourced:

    . clean-up


## Some notes

### NVIDIA injections

The docker image does not contain any NVIDIA or CUDA references, Yet, `nvidia-smi` can still be called.\
This is because the *NVIDIA Container Toolkit* (which runs on the host, not in the container) injects
the necessary files and libraries.

### SSH connection with password

It is not possible to connect to this pod with a public key (`ssh ‥ -i ‥`).

This is because I didn't create `~root/.ssh/authorized_keys`). This file seems to be created behind
the scences with my public key when using an «official» template

