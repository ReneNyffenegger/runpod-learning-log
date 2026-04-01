# Runpod pod with torch

The goal of this test was test how an image with 

## Files

### go.sh

[`go.sh`](go.sh) is the script that calls most of the scripts below in the correct order to create docker image,
template and pod.

### create-pod

[`create-pod`](create-pod) uses [`create-from-json-body`](../../API/pods/create-from-json-body) to create a pod from the image [`runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`](https://hub.docker.com/layers/runpod/pytorch/1.0.2-cu1281-torch280-ubuntu2404).

Unlike the [first pod test](../first), this pod is not created from a template.

### clean-up

[`clean-up`](clean-up) removes the pod and the template.

The script must be sourced:

    . clean-up
