# Streaming hanlder for Runpod Serverless

Setting `return_aggregate_stream` to `True` in `runpod.serverless.start()` enables output aggregation for streaming handlers.

It is intended for generator functions that use yield to produce incremental results (e.g., streaming token-by-token output from a large language model).

When enabled, the streamed pieces can be collected from the `/stream` API.
