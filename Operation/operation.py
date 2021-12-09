from Loader import OperationLoader


class Operation(OperationLoader):
    def __init__(self, name, operand_1, operand_2):
        OperationLoader.__init__(self)
        self.name = name
        self.operand_1 = operand_1
        self.operand_2 = operand_2

    def count(self):
        try:
            if self.name == "ADD":
                print(self.operand_1 + self.operand_2)
            elif self.name == "SUB":
                print(self.operand_1 - self.operand_2)
            elif self.name == "MUL":
                print(self.operand_1 * self.operand_2)
            elif self.name == 'DIV':
                print(self.operand_1 / self.operand_2)
        except ZeroDivisionError:
            print("\033[1;35mНа ноль делить нельзя\033[0m")


