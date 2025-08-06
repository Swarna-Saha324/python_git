f = open("d:/Python Code/FileInputOutput/demo.txt", "r")

data =f.read()
print(data)
print (type(data))
f.close()
f1 =open("d:/Python Code/FileInputOutput/demo1.txt", "w")
f2 =open("d:/Python Code/FileInputOutput/demo.txt", "r+")
f2.write("abc")
print(f2.read())
f2.close()
f1.write("This is a demo file")
#with syntax & automatic file closing
with open("d:/Python Code/FileInputOutput/demo.txt", "r") as f:
    data = f.read()
    print(data)
    print(type(data))
#delete the file
#module like os is used to delete the file
#import os
#os.remove("d:/Python Code/FileInputOutput/demo.txt")