# Python (Tips. Tricks. Examples)

![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)

Python programming tips and tricks. Contributions are most welcomed.

Anaconda: https://www.anaconda.com/products/individual

VS Code: https://code.visualstudio.com

Xcode: https://developer.apple.com/xcode

Jupyter: https://jupyter.org 

---

### Check similarity of two images


<img src="https://github.com/yasinnaal/images/blob/main/bb_reuslt.png?raw=true">

```
from PIL import Image
import imagehash
hash1 = imagehash.average_hash(Image.open('bike.jpg')) 
hash2 = imagehash.average_hash(Image.open('bike.jpg')) 
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
image1 average hash value: fffff704808390fe<br>
image2 average hash value: fffff704808390fe<br>
MATCH -images are similar.<br>

<img src="https://github.com/yasinnaal/images/blob/main/bp_reuslt.png?raw=true">

```
from PIL import Image
import imagehash
hash1 = imagehash.average_hash(Image.open('panda.jpg')) 
hash2 = imagehash.average_hash(Image.open('bike.jpg')) 
cutoff = 5

if hash1 - hash2 < cutoff:
  print(hash1)
  print(hash2)
  print('MATCH -images are similar.')
else:
  print('image1 average hash value:', hash1)
  print('image2 average hash value:', hash2)    
  print('NO MATCH - images are not similar !.')

```

00189c1e1fb4e080
00189c1e1fb4e080
MATCH -images are similar.


image1 average hash value: 00189c1e1fb4e080 <br>
image2 average hash value: fffff704808390fe <br>
NO MATCH - images are not similar !. <br>


<img src="https://github.com/yasinnaal/images/blob/main/bb_reuslt.png?raw=true">

```
from PIL import Image
import imagehash
hash1 = imagehash.average_hash(Image.open('panda.jpg')) 
hash2 = imagehash.average_hash(Image.open('panda.jpg')) 
cutoff = 5

if hash1 - hash2 < cutoff:
  print(hash1)
  print(hash2)
  print('MATCH -images are similar.')
else:
  print('image1 average hash value:', hash1)
  print('image2 average hash value:', hash2)    
  print('NO MATCH - images are not similar !.')
  
```

image1 average hash value: 00189c1e1fb4e080
image1 average hash value: 00189c1e1fb4e080
MATCH -images are similar.

image1 average hash value:
