# Python (Tips. Tricks. Examples)

![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)

Python programming tips and tricks. Contributions are most welcomed.

Anaconda: https://www.anaconda.com/products/individual

Jupyter: https://jupyter.org

### Check similarity of two images

```
from PIL import Image
import imagehash
hash1 = imagehash.average_hash(Image.open('/kaggle/input/myimages/bike.jpg')) 
hash2 = imagehash.average_hash(Image.open('/kaggle/input/myimages/bike.jpg')) 
cutoff = 5

if hash1 - hash2 < cutoff:
  print('image1 average hash value:', hash1)
  print('image2 average hash value:', hash2)  
  print('MATCH -images are similar.')
  
else:
  print('image1 average hash value:', hash1)
  print('image2 average hash value:', hash2)    
  print('NO MATCH - images are not similar !.')
  
```  
image1 average hash value: fffff704808390fe
image2 average hash value: fffff704808390fe
MATCH -images are similar.
