# Code Python (Easy)

![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)

Python programming tips and tricks. Contributions are most welcomed.

Anaconda: https://www.anaconda.com/products/individual

VS Code: https://code.visualstudio.com

Xcode: https://developer.apple.com/xcode

Jupyter: https://jupyter.org 

---

### Check similarity of two images

![anytext](https://github.com/yasinnaal/images/blob/main/bb_reuslt.png)

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
Result:<br>
image1 average hash value: fffff704808390fe<br>
image2 average hash value: fffff704808390fe<br>
MATCH -images are similar.<br>


![anytext](https://github.com/yasinnaal/images/blob/main/bp_reuslt.png)

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
Result:<br>
image1 average hash value: 00189c1e1fb4e080 <br>
image2 average hash value: fffff704808390fe <br>
NO MATCH - images are not similar !. <br>


![anytext](https://github.com/yasinnaal/images/blob/main/pp_reuslt.png)

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
Result:<br>
image1 average hash value: 00189c1e1fb4e080 <br>
image1 average hash value: 00189c1e1fb4e080 <br>
MATCH -images are similar. <br>

---

### Draw using Python

```
def DrawBoard(rows,cols):
    dash = " ---"
    hline = "|   "
    for i in range(0,rows):       
            print (dash * (cols))
            print (hline * (cols +1))     

DrawBoard(3, 3)

Result:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |

```

---

### FizzBuzz Challenge

The "Fizz Buzz" Challenge is an interview question designed to help filter out a lot of programming job candidates.

Write a program that prints the numbers from 1 to 100:

- For multiples of three print “Fizz” instead of the number
- For the multiples of five print “Buzz”.
- For numbers which are multiples of both three and five print “FizzBuzz”."

```

fizzbuzz = 1
while fizzbuzz <= 100:
  if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
  elif fizzbuzz % 3 == 0:
        print("Fiz")
  elif fizzbuzz % 5 == 0:
        print("Buzz")
  else:
        print(fizzbuzz)
  fizzbuzz += 1
  
  ```

1 <br>
2 <br>
Fiz <br>
4 <br>
Buzz <br>
Fiz <br>
7 <br>
8 <br>
Fiz <br>
Buzz <br>
11 <br>
Fiz <br>
13 <br>
14 <br>
FizzBuzz <br>
16 <br>
17 <br>
Fiz <br>
19 <br>
Buzz <br>
Fiz <br>
22 <br>
23 <br>
Fiz <br>
Buzz <br>
26 <br>
Fiz <br>
28 <br>
29 <br>
FizzBuzz <br>
31 <br>
32 <br>
Fiz <br>
34 <br>
Buzz <br>
Fiz <br>
37 <br>
38 <br>
Fiz <br>
Buzz <br>
41 <br>
Fiz <br>
43 <br>
44 <br>
FizzBuzz <br>
46 <br>
47 <br>
Fiz <br>
49 <br>
Buzz <br>
Fiz <br>
52 <br>
53 <br>
Fiz <br>
Buzz <br>
56 <br>
Fiz <br>
58 <br>
59 <br>
FizzBuzz <br>
61 <br>
62 <br>
Fiz <br>
64 <br>
Buzz <br>
Fiz <br>
67 <br>
68 <br>
Fiz <br>
Buzz <br>
71 <br>
Fiz <br>
73 <br>
74 <br>
FizzBuzz <br>
76 <br>
77 <br>
Fiz <br>
79 <br>
Buzz <br>
Fiz <br>
82 <br>
83 <br>
Fiz <br>
Buzz <br>
86 <br>
Fiz <br>
88 <br>
89 <br>
FizzBuzz <br>
91 <br>
92 <br>
Fiz <br>
94 <br>
Buzz <br>
Fiz <br>
97 <br>
98 <br>
Fiz <br>
Buzz <br>
