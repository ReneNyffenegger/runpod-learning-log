exampleName=minimal-pod
dockerImageName=renenyffenegger/runpod-$exampleName
templateName=$exampleName-template

. docker-build
. create-template
. create-pod

. ../../api/show-ssh-connection-details
