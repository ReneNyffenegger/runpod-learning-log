#!/usr/bin/env python3

import asyncio
from runpod_flash import Endpoint, GpuType

@Endpoint(
   name         = 'runpod-flash-hello-world',
   gpu          =  GpuType.NVIDIA_RTX_2000_ADA_GENERATION,
   dependencies =['pynvml'])
async def helloWorld():

   import pynvml

   pynvml.nvmlInit()
   hGpu    = pynvml.nvmlDeviceGetHandleByIndex(0)
   gpuName = pynvml.nvmlDeviceGetName(hGpu)
   print(f'{gpuName} says Hello world.')
   pynvml.nvmlShutdown()

   return {
      'gpuName': gpuName
   }

print(str(asyncio.run(helloWorld())))
