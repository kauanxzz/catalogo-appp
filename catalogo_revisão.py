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
# obrq: classe base. outras classes herdam dela
class Obra:
    tipo = "obra" # atributo de classe: cada subclasse sobrescreve

    def __init__(self, titulo,ano, genero):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.avaliacoes = []

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def media(self):
        if not self.avaliacoes:
            return 0.0
        soma = sum(av.nota for av in self.avaliacoes)
        return soma / len(self.avaliacoes)

    def detalhes(self):
        #informações específicas de cada tipo
        return ''

    def __str__(self):
        base = f"[{self.tipo}] {self.titulo} ({self.ano}) - {self.genero}"
        extra = self.detalhes()
        if extra:
            base += f" - {extra}"
        return f"{base} - Média: {self.media():.1f} ({len(self.avaliacoes)} avaliações)"
        
class filme(Obra):
    tipo = "filme"

    def __init__(self, titulo, ano, genero, duracao_minutos):
        super().__init__(titulo, ano, genero)
        self.duracao_minutos = duracao_minutos

    def detalhes(self):
        return f" {self.duracao_minutos} minutos"     
        
        
    
def main():
    avaliacao = Avaliacao("João", 8, "Ótima obra!")
    print(avaliacao)
    
    obra = Obra("Dom Casmurro", 1899, "Romance")
    
    obra.adicionar_avaliacao(Avaliacao("Maria", 9))
    obra.adicionar_avaliacao(Avaliacao("jose", 10))

    print("Média de avaliações:", obra.media())
    print(obra)

    filme1 = filme("Inception", 2010, "Sci-Fi", 148)
    filme1.adicionar_avaliacao(Avaliacao("Alice", 9, "Muito bom!"))
    filme1.adicionar_avaliacao(Avaliacao("Bob", 8, "Gostei, mas confuso."))
    print(filme1)   
          
if __name__ == "__main__":
    main()