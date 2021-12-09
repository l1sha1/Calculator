from Loader import OperationLoader


class SetVar(OperationLoader):
    def __init__(self, name, var_name, var_value):
        OperationLoader.__init__(self)
        self.vars = None
        self.var_name_fin = None
        self.name = name
        self.var_name = var_name
        self.var_value = var_value

    def set_var(self):
        self.var_name_fin = self.var_name
        self.var_name_fin = self.var_value
        self.vars = [self.var_name, self.var_name_fin]

    def print_var(self):
        if self.vars[0] == self.name:
            print(self.var_name_fin)
        else:
            print("FOO")
