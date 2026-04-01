# Runpod REST API examples

[API Reference overview](https://docs.runpod.io/api-reference/overview)

A [container registry auth](containerregistryauth) stores the credentials necessary to connect to a private Docker registry.
 
[Templates](templates) save pod and endpoint configurations so that they can be reused.

(Serverless) [endpoints](endpoints) are containerized applications.

[Pods](pods).

## show-ssh-connection-details

[`show-ssh-connection-details`](show-ssh-connection-details) is a helper script that waits until a pod can be connected
to and then displays the connection string, for example

     ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p 35470 root@213.173.110.22 -i ../../../_ssh/id_ed25519.runpod

This script is used in [this](../pods/first/create-pod) and [this](../pytorch/create-pod) `create-pod` scripts.
