# Code Python Tricks

![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)

Python programming tips and tricks. Contributions are most welcomed.

Anaconda: https://www.anaconda.com/products/individual

VS Code: https://code.visualstudio.com

Xcode: https://developer.apple.com/xcode

Jupyter: https://jupyter.org 

---

### Check two images similarity

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
  print('NO MATCH - images are not similar !')
```  
<br>
image1: fffff704808390fe<br>
image2: fffff704808390fe<br>
MATCH -images are similar.<br><br>


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
<br>
image1: 00189c1e1fb4e080 <br>
image2: fffff704808390fe <br>
NO MATCH - images are not similar ! <br><br>


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
<br>
image1: 00189c1e1fb4e080 <br>
image1: 00189c1e1fb4e080 <br>

MATCH -images are similar <br><br>

---

### Difference between == and = in Python

In Python and many other programming languages, a single equal mark is used to assign a value to a variable, whereas two consecutive equal marks is used to check whether 2 expressions give the same value .

= is an assignment operator

== is an equality operator

```
x=10
y=20
z=20

(x==y) is False because we assigned different values to x and y.

(y==z) is True because we assign equal values to y and z.
```

---

### What are odd numbers?

A number which is not divisible by "2" is called an odd number. An odd numbers of multi digits always ends in 1, 3, 5, 7, or 9. Examples of odd numbers: 51 , − 543 , 8765 , − 97 , 9 , etc

```
for number in range(1, 10):
    if(number % 2 != 0):
        print(number)
```
1<br>
3<br>
5<br>
7<br>
9<br>

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

#### Using the Modulo Operator %
I will use the % operator, When you see the % symbol you may think "percent" But in Python The % symbol is called the **Modulo Operator**. It returns the remainder of dividing the left hand operand by right hand operand. It's used to get the remainder of a division problem.

```
n = 1
while n <= 100:
  if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
  elif n % 3 == 0:
        print("Fiz")
  elif n % 5 == 0:
        print("Buzz")
  else:
        print(n)
  n += 1
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
