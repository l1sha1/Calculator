from Loader import OperationLoader
var = []


class Operation(OperationLoader):
    def __init__(self, name, operand_1, operand_2=None):
        OperationLoader.__init__(self)
        self.name = name
        self.operand_1 = operand_1
        self.operand_2 = operand_2 or None

    def count(self):
        try:
            if self.name == "ADD":
                if self.operand_1 == var[0]:
                    print(var[1] + float(self.operand_2))
                elif self.operand_2 == var[0]:
                    var[1] = var[1] + float(self.operand_1)
                else:
                    print(self.operand_1 + self.operand_2)

            elif self.name == "SUB":
                print(self.operand_1 - self.operand_2)
            elif self.name == "MUL":
                print(self.operand_1 * self.operand_2)
            elif self.name == 'DIV':
                print(self.operand_1 / self.operand_2)
            elif self.name == 'SET':
                if len(var) != 0:
                    del var[1]
                    del var[0]
                var.append(self.operand_1)
                self.operand_1 = self.operand_2
                var.append(self.operand_1)
            elif self.name == 'PRINT':
                if len(var) != 0 and var[0] == self.operand_1:
                    print(var[1])
                else:
                    print("\033[1;35mНе задана переменная\033[0m")
        except ZeroDivisionError:
            print("\033[1;35mНа ноль делить нельзя\033[0m")


