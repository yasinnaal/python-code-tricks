def equalcheck(num1, num2, num3):
    if int(num1) != int(num2) and int(num2) != int(num3) and int(num1 != num3):
      return False
    else:
       return True

if  equalcheck (6, "5", 5):
    print("True")       
else:
    print("False")        
