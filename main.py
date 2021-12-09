from Loader import OperationLoader
from Operation import Operation


def main():
    global var
    flag = 1
    print("****** Калькулятор ******", "       Сложение - ADD",
          "       Вычитание - SUB", "       Умножение - MUL",
          "       Деление - DIV", "Выход - exit", sep="\n")
    counter = 0
    while flag == 1:
        example = OperationLoader()
        try:
            if example.name != "False":
                Operation.count(example)
            elif example.name == "False":
                flag = 0
        except AttributeError:
            continue
        except ZeroDivisionError:
            continue
        counter += 1


if __name__ == '__main__':
    main()
