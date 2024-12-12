import os
from PIL import Image

def resize_width(img, width=538):
  default_width, default_height = img.size
  new_height = round((width/default_width)*default_height)
  resized_image = img.resize((width, new_height), Image.Resampling.LANCZOS)
  return resized_image

images_dir = os.path.join(os.path.dirname(__file__), "media/thumbnails")
for filename in os.listdir(images_dir):
  file_path = os.path.join(images_dir, filename)
  if os.path.isfile(file_path) and filename.lower().endswith(('.jpg', '.png')):
    try:
      with Image.open(file_path) as img:
        img_resized = resize_width(img) 
        img_resized.save(file_path)
        print(f"Đã resize: {filename}")
    except Exception as e:
      print(e)