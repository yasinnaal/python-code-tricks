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
  
"text": [
      "1\n",
      "2\n",
      "Fiz\n",
      "4\n",
      "Buzz\n",
      "Fiz\n",
      "7\n",
      "8\n",
      "Fiz\n",
      "Buzz\n",
      "11\n",
      "Fiz\n",
      "13\n",
      "14\n",
      "FizzBuzz\n",
      "16\n",
      "17\n",
      "Fiz\n",
      "19\n",
      "Buzz\n",
      "Fiz\n",
      "22\n",
      "23\n",
      "Fiz\n",
      "Buzz\n",
      "26\n",
      "Fiz\n",
      "28\n",
      "29\n",
      "FizzBuzz\n",
      "31\n",
      "32\n",
      "Fiz\n",
      "34\n",
      "Buzz\n",
      "Fiz\n",
      "37\n",
      "38\n",
      "Fiz\n",
      "Buzz\n",
      "41\n",
      "Fiz\n",
      "43\n",
      "44\n",
      "FizzBuzz\n",
      "46\n",
      "47\n",
      "Fiz\n",
      "49\n",
      "Buzz\n",
      "Fiz\n",
      "52\n",
      "53\n",
      "Fiz\n",
      "Buzz\n",
      "56\n",
      "Fiz\n",
      "58\n",
      "59\n",
      "FizzBuzz\n",
      "61\n",
      "62\n",
      "Fiz\n",
      "64\n",
      "Buzz\n",
      "Fiz\n",
      "67\n",
      "68\n",
      "Fiz\n",
      "Buzz\n",
      "71\n",
      "Fiz\n",
      "73\n",
      "74\n",
      "FizzBuzz\n",
      "76\n",
      "77\n",
      "Fiz\n",
      "79\n",
      "Buzz\n",
      "Fiz\n",
      "82\n",
      "83\n",
      "Fiz\n",
      "Buzz\n",
      "86\n",
      "Fiz\n",
      "88\n",
      "89\n",
      "FizzBuzz\n",
      "91\n",
      "92\n",
      "Fiz\n",
      "94\n",
      "Buzz\n",
      "Fiz\n",
      "97\n",
      "98\n",
      "Fiz\n",
      "Buzz\n"
     ]
    }
   ],
