# Streaming handler for Runpod Serverless

The handler function can return a result in pieces by using [`yield`](https://github.com/ReneNyffenegger/runpod-learning-log/blob/4e0a0f8f56b8b6c2628ee290497a1dbb841bb93c/serverless/streaming-handler/handler.py#L11).

In such a scenario, streamed pieces can be collected from the `/stream` API.

It is intended for generator functions that use yield to produce incremental results (e.g., streaming token-by-token output from a large language model).

Setting [`return_aggregate_stream`](https://github.com/ReneNyffenegger/runpod-learning-log/blob/e56643a1c2c6a9f0c12cd24412eccc08b24cf607/serverless/streaming-handler/handler.py#L16) to `True`
in [`runpod.serverless.start()`](https://github.com/ReneNyffenegger/runpod-learning-log/blob/e56643a1c2c6a9f0c12cd24412eccc08b24cf607/serverless/streaming-handler/handler.py#L14) enables
[output aggregation](https://docs.runpod.io/serverless/development/aggregate-outputs) for streaming handlers
which can be collected with `/run` or `/runsync`.\
Unfortunately, I didn't figure out how to collect the aggregated data.
