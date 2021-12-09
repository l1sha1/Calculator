from Loader import OperationLoader
from Operation import Operation
from Var import Var
from Var import SetVar


def main():
    flag = 1
    print("****** Калькулятор ******", "       Сложение - ADD",
          "       Вычитание - SUB", "       Умножение - MUL",
          "       Деление - DIV", "Выход - exit", sep="\n")
    while flag == 1:
        example = OperationLoader()
        try:
            if example.name not in ("False", "SET", "PRINT"):
                Operation.count(example)
            elif example.name == "SET":

            elif example.name == "PRINT":
                SetVar.print_var(example)
            elif example.name == "False":
                flag = 0
        except AttributeError:
            continue
        except ZeroDivisionError:
            continue


if __name__ == '__main__':
    main()
