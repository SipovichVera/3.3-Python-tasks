def read_file():
    file_name = input("enter name of file: ")
    file_name = 'hello'
    try:
        text_file = open(f"{file_name}.txt", 'r')
    except FileNotFoundError:
        print ("no such file")

    return text_file.read()


read_file()