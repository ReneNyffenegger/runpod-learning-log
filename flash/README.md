## Supported python versions

When I tried to run *runpod flash* with Python 3.14, I got the exception:
> Value error, Python 3.14 is not supported. Supported versions: 3.10, 3.11, 3.12

Thus, I had to switch to the apparently supported Python version 12:
```bash
conda create -n py-12-for-runpod-flash python=3.12
conda activate  py-12-for-runpod-flash
pip install runpod-flash
```

### Examples

[Hello world](hello-world)

## Created dot directories

Running a flash script automatically creates or populates the two dot directories
- `.runpod`
- `.flash`

This is why they're listed in the [`.gitignore`](.gitignore) file.
