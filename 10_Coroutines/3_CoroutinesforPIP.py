import asyncio
from PIL import Image

async def process_image(image_path):
    with Image.open(image_path) as img:
        await asyncio.sleep(1)
        img = img.rotate(90)
        img.save(f"processed_{image_path}")

async def process_images(image_paths):
    tasks = [process_image(image_path) for image_path in image_paths]
    await asyncio.gather(*tasks)

image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]
asyncio.run(process_images(image_paths))
