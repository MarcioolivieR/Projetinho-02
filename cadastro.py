# Projetinho-02
#estou estudando para criar app 
# Primeira página
nome = input("Nome: ")
senha = input("Senha: ")
while nome != "Marcio" or senha != "09052006":
    print("Nome ou senha incorretos!")
    nome = input("Nome: ")
    senha = input("Senha: ")
print("Acesso aprovado!")

# Segunda página
print("Bem-vindo, Marcio!")
print("Serviços disponíveis:")
print("1. Acompanhar processo")
print("2. Agendamento de prova")
print("3. Agendamento de exames")

opcao = input("Parae scolher a opção (1, 2, ou 3): ")

if opcao == "1":
    print("finalizando.")
elif opcao == "2":
    print("Prova de Legislação agendada para o dia 25/09/2024.")
elif opcao == "3":
    print("Exame médico agendado para amanhã (09/05/2028).")
else:
    print("Opção inválida. Sistema inoperante!")
