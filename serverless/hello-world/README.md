# Hello World for runpod Serverless

## go.sh

[`go.sh`](go.sh) runs the entire cycle.

First, it defines the names for
- the docker image,
- runpod template and
- runpod endpoint.

A *docker image* is
- [built](build-docker-image) from [this `Dockerfile`](Dockerfile)
- [tested locally](test-docker-iamge-locally) (with [this input](test_input.json) and
- [pushed](push-docker-image) to [docker hub](https://hub.docker.com/repository/docker/renenyffenegger/runpod-hello-world) (make sure `docker login` was executed).

The essential part of the docker image is [this handler python script](handler.py).

A [template](create-template) is built which is needed to [build the endpoint](create-endpoint).

The [endpoint is run](run-endpoint)

Finallly, the [endpoint](delete-endpoint) and [template](delete-template) are deleted.

## Observations

### Submitting a job

When submitting a job with `/runsync` or `/run`, the request must include a
JSON object with the key `"input"` containing the parameters required by
the worker's handler function, See [this link](https://docs.runpod.io/serverless/endpoints/send-requests).


### Docker image

When I tried to use `python:3.14-slim` in the `Dockerfile`, the whole exercise didn't work for no apparant reason.

