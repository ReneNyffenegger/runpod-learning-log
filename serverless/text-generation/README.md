# Text generation

```bash
$ . go.sh
$ . clean-up
```

## Observations

### Slow startup

Running an inference takes quite some time, likely because the handler function [downloads the model](https://github.com/ReneNyffenegger/runpod-learning-log/blob/458f381bd3c50d633c7f2a393ecc7f718d5482f1/serverless/text-generation/handler.py#L14) each time
it is invoked.

This observation is backed by the documentation: [Best practices for handler functions](https://docs.runpod.io/serverless/workers/handler-functions#handler-function-best-practices) points out that models
(and other heavy resources) should be loaded outside the handler function to avoid repeated initialization.

### Unable to run MiniMax M2.5

I unsuccessfully tried to run the app with the [MiniMaxAI/MiniMax-M2.5](https://github.com/ReneNyffenegger/runpod-learning-log/blob/458f381bd3c50d633c7f2a393ecc7f718d5482f1/serverless/text-generation/go.sh#L61).

First, it failed because I didn't install `accelerate` with pip in the [`Dockerfile`](Dockerfile):

    RUN  pip install --no-cache-dir runpod transformers accelerate

The error message was
> Loading an FP8 quantized model requires accelerate

After fixing that, I needed to increase the value of `containerGB` for the [template](https://github.com/ReneNyffenegger/runpod-learning-log/blob/458f381bd3c50d633c7f2a393ecc7f718d5482f1/serverless/text-generation/go.sh#L16-L31)
to a higher value of the default of 50GB because the downloaded model did not fit into
RAM (at least this was the interpretation of the content of the log file). I chose 100GB

Then, trying to run the app resulted in a timeout, so that I also increased the value of `executionTimeoutMs`
to 9999999 in the [creation of the endpoint](https://github.com/ReneNyffenegger/runpod-learning-log/blob/458f381bd3c50d633c7f2a393ecc7f718d5482f1/serverless/text-generation/go.sh#L37-L56).

After these modifications, the model would still not run. Possibly because the [chosen GPUs](https://github.com/ReneNyffenegger/runpod-learning-log/blob/458f381bd3c50d633c7f2a393ecc7f718d5482f1/serverless/text-generation/go.sh#L12) are simply not sufficient.
