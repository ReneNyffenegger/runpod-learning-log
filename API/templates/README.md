# Runpod REST API: template

Some experiments with the `template` [Runpod API](..).

## list

[`list`](list) lists templates.

## list-runpod

[`list-runpod`](list-runpod) lists runpod templates by setting the query parameter `includeRunpodTemplates` to `true` and returns the runpods' `name` and `imageName` attributes
as a «table».

## get-by-id

[`get-by-id`](get-by-id) gets the JSON object that describes a template identified by the value of `$templateId`.

## get-readme

[`get-readme`](get-readme) prints a template's readme.

The template name must be provided when calling the script:

    ./get-readme  autoresearch
    ./get-readme 'RunPod TheBloke LLMs'

## create-serverless

[`create-serverless`](create-serverless) creates a template that can be used for a serverless endpoint.

## delete

[`delete`](delete) deletes a template identified by a name

    ./delete foo-bar-template
