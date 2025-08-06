"""f1 = open(r"D:\Python Code\FileInputOutput\demo3.txt", "r+")
with open ("pratice.txt", "r") as f:
    data = f.read()
    new_data = data.replace("old", "new")
    print(new_data)
    print(type(new_data))
    with open("pratice.txt", "w") as f:
        f.write(new_data)
    f.close()"""
file_path = "D:/Python Code/FileInputOutput/demo.txt"  # use correct filename

with open(file_path, "r") as f:
    data = f.read()
    new_data = data.replace("old", "new")
    print(new_data)
    print(type(new_data))

with open(file_path, "w") as f:
    f.write(new_data)


