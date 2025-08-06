def check_word_in_file():
 word= "new"
 with open("D:/Python Code/FileInputOutput/demo.txt") as f:  # use correct filename) as f:
    data = f.read()
    if(data.find(word) != -1): #if word in data:
        print(f"The word '{word}' is found in the file.")
    else:
        print(f"The word '{word}' is not found in the file.")

check_word_in_file()

def check_word_in_line():
    word = "new"
    data =True
    line_no = 1
    with open("D:/Python Code/FileInputOutput/demo.txt") as f:  # use correct filename
        while data:
            data = f.readline()
            if (word in data):
                print(f"The word '{word}' is found in line {line_no}.")
            line_no += 1
    return -1     
    
check_word_in_line()  