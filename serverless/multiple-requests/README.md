# Multiple requests

This example shows how a single serverless container can handle many `/run` calls in sequence
and keep state between them.

## handler script behavior

A global counter (`cnt`) tracks how many times the handler has run, and each response includes both that count and the Roman numeral (`roman`) for the requested value (`val`).

## Python script for client

Unlike the [shell script](../hello-world/run-endpoint) in the [hello world](../hello-world) example, this example uses a
 Python script ([`run-endpoint.py`](run-endpoint.py)) to execute the `/run` endpoint.
