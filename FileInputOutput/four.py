with open ("d:/Python Code/FileInputOutput/demo1.txt", "r") as f:
  data = f.read()
print(data)
nums = data.split(",")
print(nums)