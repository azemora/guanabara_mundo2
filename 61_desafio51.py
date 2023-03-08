primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
iteracao = 0
while True:
    for i in range(iteracao, iteracao + 10):
        termo = primeiro_termo + i * razao
        print("Termo", i + 1, ":", termo)
    
    resposta = input("Deseja ver mais termos da PA? (s/n): ")
    if resposta.lower() == "s":
        novoval = int(input('Qual o novo termo?: '))
        iteracao += novoval
    else:
        break