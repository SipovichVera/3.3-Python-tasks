def read_file():
    file_name = input("enter name of file for reading: ")
    file = open_file(file_name, 'r')
    return file.read()


def write_into_file():
    file_name = input("enter name of file for whriting: ")
    file = open_file(file_name, 'w')
    text = input("enter some text: ")
    file.write(text)
    file.close()


def open_file(file_name, mode):
    try:
        file = open(f'{file_name}', mode)
    except FileNotFoundError:
        print("no such file")
    return file


write_into_file()
print(read_file())
