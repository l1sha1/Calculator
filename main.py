from Loader import OperationLoader
from Operation import Operation


def main():
    global var
    flag = 1
    print("****** Калькулятор ******", "       Сложение - ADD",
          "       Вычитание - SUB", "       Умножение - MUL",
          "       Деление - DIV", "Выход - exit", sep="\n")
    var = []
    counter = 0
    while flag == 1:
        example = OperationLoader()
        try:
            if example.name != "False" and example.name != "PRINT":
                if len(var) > 2:
                    del var[2]
                var.append(example.operand_1)
                Operation.count(example)
                if example.name == "SET":
                    var.append(example.operand_1)
                    print(var)
                elif counter == 0:
                    del var[0]
                else:
                    del var[2]
            elif example.name == "False":
                flag = 0
            elif example.name == "PRINT":
                if len(var) != 0 and var[0] == example.operand_1:
                    print(var)
                    print(var[1])
                else:
                    print("\033[1;35mНе задана переменная\033[0m")
        except AttributeError:
            continue
        except ZeroDivisionError:
            continue
        counter += 1


if __name__ == '__main__':
    main()
