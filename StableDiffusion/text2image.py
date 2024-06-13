import torch
from diffusers import StableDiffusion3Pipeline

pipe = StableDiffusion3Pipeline.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers", torch_dtype=torch.float16)

pipe = pipe.to("cuda")

image = pipe(
    "A cat sitting on a table",
    negative_prompt="",
    num_inference_steps=28,
    guidance_scale=7.0,
    height=256, 
    width=256,
).images[0]
image


# 目前该模型在A10下跑不了，会提示CUDA out of memory