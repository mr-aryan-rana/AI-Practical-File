import torch
from diffusers import DiffusionPipeline

# --- 1. Load the Model Pipeline ---
# This will download the model the first time you run it.
# We use torch.float16 for faster inference on a GPU.
pipeline = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
    variant="fp16"
)

# Move the pipeline to the GPU (CUDA) if available
if torch.cuda.is_available():
    pipeline.to("cuda")
else:
    print("CUDA not available. Running on CPU (this will be very slow).")

# --- 2. Define Your Prompts ---
# 'prompt' is what you WANT to see
prompt = "An astronaut riding a horse on Mars, high quality, digital art"

# 'negative_prompt' is what you DON'T want to see (optional but recommended)
negative_prompt = "blurry, low quality, bad anatomy, text, watermark"

# --- 3. Generate the Image ---
# num_inference_steps: More steps can mean higher quality, but 25-50 is typical.
# guidance_scale: How strongly the image should follow the prompt. 7.5 is a good default.
print("Generating image...")
image = pipeline(
    prompt=prompt,
    negative_prompt=negative_prompt,
    num_inference_steps=30,
    guidance_scale=7.5
).images[0]  # The output is a list of images, we take the first one

# --- 4. Save the Image ---
image.save("astronaut_on_mars.png")
print("Image saved as 'astronaut_on_mars.png'")