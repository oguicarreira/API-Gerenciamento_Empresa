class Veiculo:
    def __init__(self, id, modelo, ano, categoria, marca=None):
        self.id = id
        self.modelo = modelo
        self.ano = ano
        self.categoria = categoria
        self.marca = marca

    def __repr__(self):
        return f"<Veiculo {self.modelo}, {self.ano}>"