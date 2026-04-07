# Runpod SDK: Hello world

This *hello world* example tries to demonstrate the basics of the [Runpod SDK](..).

It uses the same [Docker image](https://hub.docker.com/r/renenyffenegger/runpod-serverless-hello-world) as also
the [serverless hello world example](../../serverless/hello-world).

## Observersions

### No delete method for endpoints and templates

Althoug there is `runpod.create_template` and `runpod.create_endpoint`, I've found no method to delete endpoints and/or templates
