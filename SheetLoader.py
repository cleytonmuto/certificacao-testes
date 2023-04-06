import pandas

class SheetLoader:

    def __init__(self):
        pass

    def run(self):
        planilha = pandas.read_excel("usuarios.xlsx", index_col = 0)
        print(planilha)
        print()
        print(planilha.to_csv())

teste = SheetLoader()
teste.run()

