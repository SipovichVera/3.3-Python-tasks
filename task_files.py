class File:

    def read_file(self, file_name):
        try:
            with open(f'{file_name}', 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "no such file"


    def write_into_file(self, file_name, text):
        with open(f'{file_name}', 'w') as file:
            file.write(text)
        file.close()


def test_file():
    file = File()
    file_name = input("enter name of file for reading: ")
    print(file.read_file(file_name))

    file_name = input("enter name of file for whriting: ")
    text = input("enter some text: ")
    file.write_into_file(file_name, text)


test_file()