import runpod
from transformers import pipeline, GenerationConfig

def handler(job):

    try:

       job_input = job["input"]

       prompt    = job_input.get('prompt'  , 'Say something'           )
       model     = job_input.get('model'   , 'Qwen/Qwen2.5-3B-Instruct')
       hf_token  = job_input.get('HF_TOKEN', ''                        )

       genpip = pipeline('text-generation', model = model, token=hf_token)

       result = genpip(prompt, generation_config = GenerationConfig(max_new_tokens=99, token = hf_token))

       return {
           'result' : result[0]['generated_text']
       }


    except Exception as e:
       return {
          "error"           : str(e),
          "error-type"      : str(type(e))
       }

result = runpod.serverless.start({"handler": handler})
