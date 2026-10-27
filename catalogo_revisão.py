# avaliacao: oq o usuario escreve sobre uma obra

class Avaliacao:
    def __init__(self, autor, nota, comentario = ""):
        if not 0 <= nota <= 10:
            raise ValueError("Nota deve estar entre 0 e 10")
        self.autor = autor
        self.nota = nota
        self.comentario = comentario



    def __str__(self):
        texto = f"{self.autor}: {self.nota}/10"
        if self.comentario:
            texto += f' - "{self.comentario}"'
            return texto
def main():
    avaliacao = Avaliacao("João", 8, "Ótima obra!")
    print(avaliacao)


if __name__ == "__main__":
    main()