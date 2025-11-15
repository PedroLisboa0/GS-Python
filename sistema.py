class SistemaOrientacaoCarreiras:
    def __init__(self, Motor):
        self.perfis = []
        self.motor = Motor()

    def adicionar_perfil(self, perfil):
        self.perfis.append(perfil)

    def analisar_perfil(self, nome: str):
        for perfil in self.perfis:
            if perfil.nome == nome:
                print("Carreiras sugeridas:")
                carreiras = self.motor.recomendar_carreiras(perfil)
                for carreira, valor in carreiras:
                    print(f"{carreira} (score: {valor})")

                print("Trilhas de aprendizado:")
                trilhas = self.motor.recomendar_trilhas(perfil)
                if trilhas:
                    for comp, trilha in trilhas:
                        print(f"- Melhorar '{comp}': {trilha}")
                else:
                    print("Nenhuma trilha necessária.")

                print("\n=======================================")
                return

        print("Perfil não encontrado.")