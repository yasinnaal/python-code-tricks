#simple if else
X = 5
if X == 5:
    print("X = ", X)
else:
    print("simple if else")

#Naseted if else
print("A) Read the file")
print("B) Delete the file and start over")
print("C) Append the file")
user_choice = input("Please enter choice: ")


if user_choice == "A":
   print("user choice A")
elif user_choice == "B":
     print("user choice B")
elif user_choice == "C":
     print("user choice C")
else:      
     print("please enter A or B or C")