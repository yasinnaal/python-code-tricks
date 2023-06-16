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
 1
2
Fiz
4
Buzz
Fiz
7
8
Fiz
Buzz
11
Fiz
13
14
FizzBuzz
16
17
Fiz
19
Buzz
Fiz
22
23
Fiz
Buzz
26
Fiz
28
29
FizzBuzz
31
32
Fiz
34
Buzz
Fiz
37
38
Fiz
Buzz
41
Fiz
43
44
FizzBuzz
46
47
Fiz
49
Buzz
Fiz
52
53
Fiz
Buzz
56
Fiz
58
59
FizzBuzz
61
62
Fiz
64
Buzz
Fiz
67
68
Fiz
Buzz
71
Fiz
73
74
FizzBuzz
76
77
Fiz
79
Buzz
Fiz
82
83
Fiz
Buzz
86
Fiz
88
89
FizzBuzz
91
92
Fiz
94
Buzz
Fiz
97
98
Fiz
Buzz
