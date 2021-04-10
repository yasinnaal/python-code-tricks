
# | |    0
#-----  1
# | |   2
#-----  3
# | |   4
# 01234
 

for row in range (5): # 0,1,2,3,4
    if row%2 == 0:
       for col in range (5): # 0,1,2,3,4
            if col%2 == 0:
                if col != 4: #end of the line (loop end)
                   print(" ", end="")
                else:
                   print(" ")
            else:
                 print("|", end="")
    else:
        print("-----")                
