exampleName=minimal-pod
dockerImageName=renenyffenegger/runpod-$exampleName
templateName=$exampleName-template

. docker-build
. create-template
. create-pod

. ../../API/show-ssh-connection-details
