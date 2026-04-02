# Hello World for runpod Serverless

An attempt to create a *Hello World* app for [runpod Serverless](..).

## go.sh

[`go.sh`](go.sh) runs the entire cycle.

- It defines the names for
  - the docker image,
  - runpod template and
  - runpod endpoint.
- A *docker image* is
  - [built](build-docker-image) from [this `Dockerfile`](Dockerfile)
  - [tested locally](test-docker-image-locally) (with [this input](test_input.json)) and
  - [pushed](push-docker-image) to [docker hub](https://hub.docker.com/repository/docker/renenyffenegger/runpod-serverless-hello-world) (make sure `docker login` was executed).
- A [template](create-template) is built which is needed to [build the endpoint](create-endpoint).
- The [endpoint is run](run-endpoint)
- The [endpoint](delete-endpoint) and [template](delete-template) are deleted

## handler.py

The essential part of the docker image is [the python handler script `handler.py`](handler.py).

### Environment variables

The script determines the values of the two environment variables
- [`ENV_VAR_FROM_DOCKERFILE`](https://github.com/ReneNyffenegger/runpod-learning-log/blob/c3d8214d14508a805d3969a66d305e4e8c618209/serverless/hello-world/handler.py#L25) and
- [`ENV_VAR_FROM_TEMPLATE`](https://github.com/ReneNyffenegger/runpod-learning-log/blob/c3d8214d14508a805d3969a66d305e4e8c618209/serverless/hello-world/handler.py#L26)

The first is [assigned](https://github.com/ReneNyffenegger/runpod-learning-log/blob/c3d8214d14508a805d3969a66d305e4e8c618209/serverless/hello-world/Dockerfile#L3-L4) in the Dockerfile from the value
passed using `--build-arg ‥` in [`build-docker-image`](build-docker-image).

The second is [set](https://github.com/ReneNyffenegger/runpod-learning-log/blob/c3d8214d14508a805d3969a66d305e4e8c618209/serverless/hello-world/create-template#L21) when the template is created.

## Observations

### Submitting a job

When submitting a job with `/runsync` or `/run`, the request must include a
JSON object with the key `"input"` containing the parameters required by
the worker's handler function, See [this link](https://docs.runpod.io/serverless/endpoints/send-requests).


### Docker image

When I tried to use `python:3.14-slim` in the `Dockerfile`, the whole exercise didn't work for no apparant reason.

