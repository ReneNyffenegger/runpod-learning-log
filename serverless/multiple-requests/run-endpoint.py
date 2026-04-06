#!/usr/bin/env python3
# vim: foldmethod=marker foldmarker={{{,}}}

import json
import os
import sys
import time

import requests

API_BASE = "https://api.runpod.ai/v2"

def call_api(endpoint_id, api_key, path, payload=None):  # {{{
    url = f"{API_BASE}/{endpoint_id}{path}"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    if payload:
       res = requests.post(url, headers=headers, json=payload, timeout=2)
    else:
       res = requests.get(url, headers=headers, timeout=2)
    return res.json()

# }}}

def submit_job(endpoint_id, api_key, val):  # {{{
    payload = {'input': {'val': val}}
    return call_api(endpoint_id, api_key, '/run', payload=payload)
# }}}

def fetch_status(endpoint_id, api_key, job_id):  # {{{
    return call_api(endpoint_id, api_key, f'/status/{job_id}')
# }}}

# {{{ main

API_KEY = os.getenv('RUNPOD_API_KEY')
if not API_KEY:
    print('Missing RUNPOD_API_KEY environment variable')
    quit()

endpointId =     sys.argv[1]
val        = int(sys.argv[2])

# submit_job returns a dict
res = submit_job(endpointId, API_KEY, val)

jobId = res.get('id')
print(f'jobId = {jobId}')

spinner_chars = ['|', '/', '-', '\\']
spinner_index = 0

sys.stdout.write('\033[?25l') # Hide cursor

st = res.get('status')
while st in {'IN_QUEUE', 'IN_PROGRESS'}:

  #
  # Half a rotation for the spinner in a second:
  #
    for spinner_index in range(4):
        spinner_char = spinner_chars[spinner_index]
        sys.stdout.write(f"\r\033[Kstatus = {st} {spinner_char}")

        time.sleep(0.25) 

    res = fetch_status(endpointId, API_KEY, jobId)
    st = res.get('status')

sys.stdout.write('\033[?25h') # show cursor again

# Clear line with spinner character
sys.stdout.write('\r\033[K')

if st == 'COMPLETED':
    output = res.get('output') or {}
    cnt = output.get('cnt'  )
    rom = output.get('roman')
    print(f'cnt={cnt} | val = {val} - roman = {rom}\n')
    sys.exit(0)

print(f'status = {st}')
print(json.dumps(res, indent=2))

# }}}
