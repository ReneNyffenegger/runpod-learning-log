exampleName=streaming
dockerImageName=renenyffenegger/runpod-serverless-$exampleName:latest
templateName=$exampleName-template
endpointName=$exampleName-world-endpoint

. docker-image

. create-template
. create-endpoint

. run-endpoint

. cleanup
