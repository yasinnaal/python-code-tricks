from PIL import Image
import imagehash
hash0 = imagehash.average_hash(Image.open('quora_photo.jpg')) 
hash1 = imagehash.average_hash(Image.open('twitter_photo.jpeg')) 
cutoff = 5

if hash0 - hash1 < cutoff:
  print('images are similar')
else:
  print('images are not similar')