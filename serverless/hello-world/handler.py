#!/usr/bin/env python3

import runpod
import sys
import os

def handler(job):

    inputData = job['input']
    
    name = inputData.get('name', 'World')
    val1 = inputData.get('val1',      1 )
    val2 = inputData.get('val2',    100 )
    
  # The calculated result
    return {
      'greeting'      : f'Hello {name}' ,
      'product'       : val1 * val2     ,
      'sum'           : val1 + val2     ,
      'job-id'        : job.get('id'       , 'n/a'),
      'job-status'    : job.get('status'   , 'n/a'),
      'delay-time'    : job.get('delayTime', 'n/a'),
      'job-keys'      : str(job.keys())            , # job is a dict (or at least dict like)
      'python-version': sys.version,
      'ENV_VAR_1'     : os.getenv('ENV_VAR_1', 'n/a'),
      'ENV_VAR_2'     : os.getenv('ENV_VAR_2', 'n/a')
   }

runpod.serverless.start({'handler': handler})
