
#qmacro Thinking Aloud

categories  = ["Major", "Minor", "Mini", "Micro"]
blog = ["qmacro.org SAP Community", "autodidactics", "(something missing)", "Twitter"]
blog_e_length = len(blog)
blog_c_length = sum(len(i) for i in blog)
hdash = "-"* (blog_e_length + blog_c_length)
def DrawBoard(rows,cols):   
    print(hdash)
    for r1 in range(0,cols):       
            line1length = len(blog[r1]) -  len (categories[r1])            
            print(categories[r1] + " " * line1length  + "|", end = '')
    print()  
    for r2 in range(0,cols):       
            print(blog[r2] + ""  + "|", end = '')
    print()   
    print(hdash)
DrawBoard(2, len(categories))