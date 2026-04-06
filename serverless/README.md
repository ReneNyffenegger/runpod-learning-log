# Runpod Serverless

## Tests

[Hello world](hello-world)

[Multiple requests](multiple-requests) show how a singe serverless container can handle many `/run` calls in sequence and keep state between them.

[Streaming handler](streaming-handler) demonstrates a streaming hanlder, which allows to return a (potentially large) result to the client in multiple pieces.

[Text generation](text-generation)

## Serverless handler function

In a Python serverless application, the *serverless handler function* is indirectly invoked via `runpod.serverless.start` (as for example in the [hello world example](https://github.com/ReneNyffenegger/runpod-learning-log/blob/d0db37379d749a9b28cdf25a70c393e4923da553/serverless/hello-world/handler.py#L29)).

The hander script is started by a [`CMD [ "python", "-u", "handler.py"]`](https://github.com/ReneNyffenegger/runpod-learning-log/blob/d0db37379d749a9b28cdf25a70c393e4923da553/serverless/hello-world/Dockerfile#L10) directive in the `Dockerfile`.

In the source code of the the `runpod` library, `runpod.serverless.start` is found [here](https://github.com/runpod/runpod-python/blob/3a5f8c7d500fc57092a35da55d5f5a555effe512/runpod/serverless/__init__.py#L135).
