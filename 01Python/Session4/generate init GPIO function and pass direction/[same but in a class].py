import os

class FileWriter:
    name=""
    def __init__(self,name):
        self.mypath = os.path.dirname(os.path.realpath(__file__)) + name

    def write_init(self):
        bits = "0b" + self.user_selection()
        init = f"void Init_PORTA_DIR(void){{\n\
        DDRA = {bits};\n\
        }}\n"

        print(init)

        with open(self.mypath, 'a') as fd:
            fd.write(init)

    def user_selection(self):
        list = []
        for i in range(0, 8):
            while True:
                user_input = input(f"Please enter bit {i} mode:")
                if user_input == "in":
                    list.append(0)
                    break
                elif user_input == "out":
                    list.append(1)
                    break
                else:
                    print("Please enter a valid direction")

        # Reverse bits, and join them to be a string
        list.reverse()
        bits = ''.join(map(str, list))
        return bits
    def __del__():
        pass

if __name__ == "__main__":
    file_writer = FileWriter("/init.c")
    file_writer.write_init()
