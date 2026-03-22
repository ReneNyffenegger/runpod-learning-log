dockerImageName=renenyffenegger/runpod-hello-world:latest
templateName=hello-world-template
endpointName=hello-world-endpoint

. build-docker-image
. test-docker-image-locally
. push-docker-image

. create-template
. create-endpoint

. run-endpoint

. delete-endpoint
. delete-template
