from sistema import SistemaOrientacaoCarreiras
from perfil import Perfil
from motor import MotorRecomendacao

def exibir_menu():
    print("\n" + "="*50)
    print("SISTEMA DE ORIENTAÇÃO DE CARREIRAS")
    print("="*50)
    print("1. Exibir perfis cadastrados")
    print("2. Adicionar novo perfil")
    print("3. Analisar perfil")
    print("4. Sair")
    print("="*50)

def exibir_perfis(sistema):
    if not sistema.perfis:
        print("\nNenhum perfil cadastrado.")
        return
    
    print("\n--- Perfis Cadastrados ---")
    for i, perfil in enumerate(sistema.perfis, 1):
        print(f"{i}. {perfil.nome}")
        print(f"   Competências: {perfil.competencias}")
    print()

def adicionar_novo_perfil(sistema):
    print("\n--- Adicionar Novo Perfil ---")
    nome = input("Digite o nome do perfil: ").strip()
    
    if not nome:
        print("Nome não pode estar vazio!")
        return
    
    competencias = {}
    competencias_disponiveis = [
        "logica", "criatividade", "colaboracao", "adaptabilidade",
        "estatistica", "comunicacao", "raciocinio_analitico", "resolucao_problemas",
        "pensamento_critico", "empatia", "organizacao", "analise_de_dados",
        "atencao_detalhes", "inovacao"
    ]
    
    print("\nDigite as competências e suas pontuações (0-10):")
    print("Competências disponíveis: " + ", ".join(competencias_disponiveis))
    
    while True:
        comp = input("\nCompetência (ou 'pronto' para finalizar): ").strip().lower()
        
        if comp == "pronto":
            if not competencias:
                print("Adicione pelo menos uma competência!")
                continue
            break
        
        if comp not in competencias_disponiveis:
            print(f"Competência '{comp}' não reconhecida. Tente novamente.")
            continue
        
        try:
            valor = int(input(f"Pontuação para '{comp}' (0-10): "))
            if 0 <= valor <= 10:
                competencias[comp] = valor
                print(f"'{comp}' adicionada com valor {valor}")
            else:
                print("Pontuação deve estar entre 0 e 10!")
        except ValueError:
            print("Digite um número válido!")
    
    perfil = Perfil(nome, competencias)
    sistema.adicionar_perfil(perfil)
    print(f"\nPerfil '{nome}' adicionado com sucesso!")

def analisar_perfil(sistema):
    if not sistema.perfis:
        print("\nNenhum perfil cadastrado para análise.")
        return
    
    print("\n--- Analisar Perfil ---")
    exibir_perfis(sistema)
    
    nome = input("Digite o nome do perfil para análise: ").strip()
    print()
    sistema.analisar_perfil(nome)

def main():
    sistema = SistemaOrientacaoCarreiras(Motor=MotorRecomendacao)
    
    # Criar um perfil padrão
    competencias_alexandre = {
        "logica": 6,
        "criatividade": 8,
        "colaboracao": 10,
        "adaptabilidade": 7,
        "estatistica": 5,
        "comunicacao": 10
    }
    
    perfil_alexandre = Perfil("Alexandre", competencias_alexandre)
    sistema.adicionar_perfil(perfil_alexandre)
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            exibir_perfis(sistema)
        elif opcao == "2":
            adicionar_novo_perfil(sistema)
        elif opcao == "3":
            analisar_perfil(sistema)
        elif opcao == "4":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
