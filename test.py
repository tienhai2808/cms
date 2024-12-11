from PIL import Image

img = Image.open('C:/Users/NITRO/Downloads/favicon.png')
img_resized = img.resize((150, 28), Image.Resampling.LANCZOS)
img_resized.save('C:/Users/NITRO/Downloads/favicon.png')