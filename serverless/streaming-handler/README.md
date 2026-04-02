# Streaming handler for Runpod Serverless

Setting [`return_aggregate_stream`](https://github.com/ReneNyffenegger/runpod-learning-log/blob/f5a28169370bc15be6500b75891723ac9f2ed9d7/serverless/streaming-handler/handler.py#L16) to `True`
 in [`runpod.serverless.start()`](https://github.com/ReneNyffenegger/runpod-learning-log/blob/f5a28169370bc15be6500b75891723ac9f2ed9d7/serverless/streaming-handler/handler.py#L14) enables output aggregation for streaming handlers.

It is intended for generator functions that use yield to produce incremental results (e.g., streaming token-by-token output from a large language model).

When enabled, the streamed pieces can be collected from the `/stream` API.
