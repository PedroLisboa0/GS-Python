class Perfil:
    def __init__(self, nome: str, competencias: dict):
        self.nome = nome
        self.competencias = competencias # competências espera um dicionário no formato "competencia" : valor.

    def __str__(self):
        return f"Perfil de {self.nome} | Competências: {self.competencias}"