#!/usr/bin/env python3

import runpod
import time

def streamer(job):

    pieces = job['input'].get('pieces', 10)

    for piece in range(pieces):
        yield {"piece": piece, "timestamp": time.strftime("%H:%M:%S", time.gmtime())}
        time.sleep(1)

runpod.serverless.start({
    "handler"                : streamer,
    "return_aggregate_stream": True      # If set to True, aggregated output can be queried also with /run or /runsync
})
