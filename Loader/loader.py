

class OperationLoader:
    def __init__(self):
        try:
            frase = input("Введите операцию ")
            self.o_list = frase.split(' ')
            self.name = self.o_list[0]
            if self.name not in ("exit", "SET", "PRINT"):
                self.operand_1 = self.o_list[1]
                self.operand_2 = self.o_list[2]
            elif "exit" in frase:
                self.name = "False"
            elif "SET" in frase:
                self.name = self.o_list[0]
                self.operand_1 = str(self.o_list[1])
                self.operand_2 = float(self.o_list[2])
            elif "PRINT" in frase:
                self.name = self.o_list[0]
                self.operand_1 = str(self.o_list[1])
            if self.name not in ("ADD", "SUB", "MUL", "DIV", "False", "SET", "PRINT"):
                print("\033[1;35mНеизвестная операция\033[0m")
        except ValueError:
            print("\033[1;35mНеверное значение операнда\033[0m")
        except IndexError:
            print("\033[1;35mПропущены значения операнда\033[0m")
