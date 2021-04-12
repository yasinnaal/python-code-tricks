import os.path
from os import path

file_path = input("Please Enter file name: ")
#file_path = "E:/Python/note-taking.txt"
file_path = ("E:/Python/" + file_path)
#file_exist = os.path.exists('E:/Python/note-taking.txt')
#file_exist = os.path.exists('E:/Python/' + file_path)
file_exist = os.path.exists(file_path)

if file_exist == False:
    print("File does not exist")
else:
     print("File",file_path , "already exist please select one choice")
     print("A) Read the file")
     print("B) Delete the file and start over")
     print("C) Append the file")
     user_choice = input()

     if user_choice == "A": # Read the file
        myfile = open('E:/Python/note-taking.txt', 'r')  
        file_text = myfile.read()  
        myfile.close()    
        print(file_text)

     elif user_choice == "B": # Delete the file and start over          
          myfile = open('E:/Python/note-taking.txt', 'w')  
          myfile.close()    
          print("file deleted, new file created")       

     elif user_choice == "C": # Append to the file          
          add_text = input("Please Enter text to add ")
          myfile = open('E:/Python/note-taking.txt', 'a')  
          add_text = myfile.writelines(add_text)
          myfile.close()
          print("texr added to file successfully")       
          
     else: 
          print("you didn't enter correct choice ")     

          


