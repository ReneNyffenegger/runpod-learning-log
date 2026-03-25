if [ -z "${RUNPOD_API_KEY}" ]; then
   echo "RUNPOD_API_KEY is not set"
   return 1
fi

exampleName=text-generation

dockerImageName=renenyffenegger/runpod-serverless-$exampleName
templateName=$exampleName-template
endpointName=$exampleName-texts-endpoint

gpus='"NVIDIA RTX A4000","NVIDIA RTX A4500","NVIDIA RTX 4000 Ada Generation","NVIDIA RTX 2000 Ada Generation"'

. docker-build

templateId=$(curl -sS https://rest.runpod.io/v1/templates   \
  -H  'Content-Type: application/json'         \
  -H  "Authorization: Bearer $RUNPOD_API_KEY"  \
  -d @- <<DATA     | jq -r .id
{
  "imageName"              : "$dockerImageName",
  "name"                   : "$templateName",
  "isServerless"           :  true,
  "isPublic"               :  false,
  "category"               : "NVIDIA",
  "containerDiskInGb"      :  50,
  "readme"                 : "",
  "volumeInGb"             : -1
}
DATA
)


echo created template with id $templateId


endpointId=$(curl -sS https://rest.runpod.io/v1/endpoints \
  -H  'Content-Type: application/json'         \
  -H  "Authorization: Bearer $RUNPOD_API_KEY"  \
  -d @- <<DATA     | jq -r .id
{
  "templateId"        : "$templateId",
  "computeType"       : "GPU",
  "flashboot"         :  true,
  "gpuCount"          :  1,
  "gpuTypeIds"        : [ $gpus ],
  "idleTimeout"       :  5,
  "minCudaVersion"    : "12.0",
  "name"              : "$endpointName",
  "scalerType"        : "QUEUE_DELAY",
  "scalerValue"       :  4,
  "workersMax"        :  3,
  "workersMin"        :  0
}
DATA
)

echo created endpoint with id $endpointId

. run-endpoint Qwen/Qwen2.5-3B-Instruct   Explain an AI transformer
# run-endpoint MiniMaxAI/MiniMax-M2.5     Why do many programmers drink coffee?
. run-endpoint Qwen/Qwen2.5-3B-Instruct   Why do many programmers drink coffee?
