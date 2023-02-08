
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

for i in range(10):
    termo = primeiro_termo + i * razao
    print("Termo", i + 1, ":", termo)

