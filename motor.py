class MotorRecomendacao:
    def __init__(self):
        # Cada carreira possui três competências que serão utilizadas para recomendá-la.
        self.carreiras = {
            "Desenvolvedor de Software": ("logica", "raciocinio_analitico", "resolucao_problemas"),
            "Cientista de Dados": ("logica", "estatistica", "pensamento_critico"),
            "Designer UX/UI": ("criatividade", "empatia", "comunicacao"),
            "Gestor de Projetos": ("colaboracao", "organizacao", "comunicacao"),
            "Especialista em IA": ("logica", "estatistica", "inovacao"),
            "Marketing Digital": ("criatividade", "analise_de_dados", "comunicacao"),
            "Cibersegurança": ("logica", "atencao_detalhes", "resolucao_problemas"),
        }

        # Trilhas de aprendizado sugeridas.
        self.trilhas = {
            "logica": "Curso de Lógica de Programação, Python básico",
            "criatividade": "Design Thinking, Cursos de UX",
            "colaboracao": "Scrum, Comunicação não-violenta",
            "adaptabilidade": "Cursos sobre Resiliência e Mudanças",
            "estatistica": "Estatística Aplicada, Probabilidade",
            "inovacao": "Criatividade aplicada e IA",
            "comunicacao": "Oratória, Escrita Profissional",
        }

    def recomendar_carreiras(self, perfil):
        pontuacoes = {}

        for carreira, competencias_relevantes in self.carreiras.items():
            score = 0
            for comp in competencias_relevantes:
                score += perfil.competencias.get(comp, 0)
            pontuacoes[carreira] = score

        # Ordenar por pontuação
        recomendacoes = sorted(pontuacoes.items(), key=lambda x: x[1], reverse=True)
        return recomendacoes[:3]  # Top 3 carreiras

    def recomendar_trilhas(self, perfil):
        trilhas = []
        for comp, valor in perfil.competencias.items():
            if valor < 6 and comp in self.trilhas:
                trilhas.append((comp, self.trilhas[comp]))
        return trilhas
