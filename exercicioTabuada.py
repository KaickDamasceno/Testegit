
# Exercício 9 - FAÇA UMA TABUADA PERSONALIZADA
#SEU SISTEMA DEVE PEDIR UM NÚMERO PARA O USUÁRIO E LOGO EM SEGUIDA A TABUADA DAQUELE NÚMERO DEVE SER CALCULADA
#CADA RESULTADO PRECISA SER DEMONSTRADO

num = int(input("Digite o número para a tabuada: "))

print (f"A tabuada do número: {num}")

for i in range(1, 11):
    resultado = num * i
    print (f"{num} * {i} = {resultado}")
