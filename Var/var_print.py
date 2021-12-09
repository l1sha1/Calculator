from Var import SetVar


class Var(SetVar):
    def __init__(self, name, var_name):
        SetVar.__init__(self, self.var_name_fin)
        self.name = name
        self.var_name = var_name
        print(self.var_name)
        print(self.var_name_fin)


    def print_var(self):
        print(self.var_name_fin)