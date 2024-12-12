from PIL import Image
from io import BytesIO
from django.core.files.images import ImageFile

def viewed_auth(request, user):
  profile = user.profile
  session_viewed = request.session.get('recently_viewed', [])
  profile_viewed = profile.recently_viewed
  combined_viewed = list(dict.fromkeys(profile_viewed + session_viewed))[:10]
  profile.recently_viewed = combined_viewed
  profile.save()
  request.session['recently_viewed'] = combined_viewed
  request.session.modified = True
  
def resize_width(img, width):
  image = Image.open(img)
  default_width, default_height = image.size
  new_height = round((width/default_width)*default_height)
  resized_image = image.resize((width, new_height), Image.Resampling.LANCZOS)
  image_data = BytesIO()
  resized_image.save(fp=image_data, format=img.image.format)
  image_file = ImageFile(image_data)
  return image_file