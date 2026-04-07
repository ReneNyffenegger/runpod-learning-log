#!/usr/bin/env python3
# vim: foldmethod=marker foldmarker={{{,}}}

import os
import time
import runpod

runpod.api_key = os.getenv('RUNPOD_API_KEY')
if runpod.api_key == None:
   print('Env var RUNPOD_API_KEY is not set')
   quit()

template = runpod.create_template(
    name          ='sdk-hello-world-template',
    image_name    ='renenyffenegger/runpod-serverless-hello-world',
    is_serverless = True
)

endpoint_ = runpod.create_endpoint(
   name        ='sdk-hello-world-endpoint',
   template_id = template['id'],
   gpu_ids     ='AMPERE_16', # Comma separated value of GPU Pools, not GPU models! https://docs.runpod.io/references/gpu-types#gpu-pools
   workers_min = 0,
   workers_max = 1,
   flashboot   = True,
   gpu_count   = 1           # gpu_count cannot be set to 0, unfortunately.
)

endpoint = runpod.Endpoint(endpoint_['id'])

job = endpoint.run({
    'name': 'René',
    'val1':  2    ,
    'val2':  3
})

while True:

    st = job.status()
    if st == 'COMPLETED': break
    print(st)
    time.sleep(1)

result = job.output()

print('Run result:')
print(f"  greeting               : {result['greeting']               }")
print(f"  sum                    : {result['sum']                    }")
print(f"  product                : {result['product']                }")
print(f"  python-version         : {result['python-version']         }")
print(f"  ENV_VAR_FROM_DOCKERFILE: {result['ENV_VAR_FROM_DOCKERFILE']}")
print(f"  ENV_VAR_FROM_TEMPLATE  : {result['ENV_VAR_FROM_TEMPLATE']  }")
print(f"  delay-time             : {result['delay-time']             }")
print(f"  job-id                 : {result['job-id']                 }")
print(f"  job-keys               : {result['job-keys']               }")
print(f"  job-status             : {result['job-status']             }")
