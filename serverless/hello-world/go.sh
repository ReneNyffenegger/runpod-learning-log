exampleName=hello-world
dockerImageName=renenyffenegger/runpod-serverless-$exampleName:latest
templateName=$exampleName-template
endpointName=$exampleName-endpoint

. build-docker-image
. test-docker-image-locally
. push-docker-image

. create-template
. create-endpoint

. run-endpoint

. delete-endpoint
. delete-template
