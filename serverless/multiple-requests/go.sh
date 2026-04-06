exampleName=multiple-requests
dockerImageName=renenyffenegger/runpod-serverless-$exampleName:latest
templateName=$exampleName-template
endpointName=$exampleName-endpoint

. build-docker-image

. create-template
. create-endpoint

python3 run-endpoint.py $endpointId 42
python3 run-endpoint.py $endpointId 99
python3 run-endpoint.py $endpointId 16

. clean-up
