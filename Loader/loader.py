class OperationLoader:
    def __init__(self):

        frase = input("Введите операцию ")
        self.o_list = frase.split(' ')
        self.name = self.o_list[0]
        if self.name not in ("exit", "SET", "PRINT"):
            self.operand_1 = float(self.o_list[1])
            self.operand_2 = float(self.o_list[2])
        elif "exit" in frase:
            self.name = "False"
        elif "SET" in frase:
            self.name = self.o_list[0]
            self.var_name = str(self.o_list[1])
            self.var_value = float(self.o_list[2])
        elif "PRINT" in frase:
            self.name = self.o_list[0]
            self.var_name = str(self.o_list[1])
            # if self.name not in ("ADD", "SUB", "MUL", "DIV", "False"):
            # print("\033[1;35mНеизвестная операция\033[0m")
        # except ValueError:
        # print("\033[1;35mНеверное значение операнда\033[0m")
