class EstoquePassivo:
    def __init__(self, id, nome, descricao, preco, quantidade):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.preco * self.quantidade

    def __repr__(self):
        return f"<EstoquePassivo {self.nome}, Qtd: {self.quantidade}, Preço: {self.preco}>"