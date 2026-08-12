                    # Nível 1: 
                    # Crie um programa que faça o seguinte:
                    #  Peça para o usuário digitar o peso (em quilos).
                    # Peça para o usuário digitar a altura (em metros).
                    # Calcule o IMC usando a fórmula: peso / (altura * altura).
                    # Exiba o resultado final na tela.

# peso = float(input("Digite o seu peso (kg): ").replace(",","."))
# altura = float(input("Digite a sua altura (m): ").replace(",","."))

# imc = peso / (altura * altura)

# print(f"\nO seu IMC é: {imc:.2f}")

# # Nível 2: Adicionando Condições (If/Else)Modifique o programa anterior para que ele avalie o resultado:
# # Se o IMC for menor que 18.5, exiba: "Abaixo do peso".
# # Se o IMC estiver entre 18.5 e 24.9, exiba: "Peso normal"
# # .Se o IMC for 25 ou mais, exiba: "Acima do peso".

# if imc <18.5:
#     print ("Abaixo do peso")
# elif imc  <=24.9:
#     print ("Peso normal")
# else:
#     print ("Acima do peso.")    
#=========================================================================

# while True:
#     peso = float(input("Digite o seu peso (kg): ").replace(",","."))
#     altura = float(input("Digite a sua altura (m): ").replace(",","."))

#     imc = peso / (altura * altura)  

#     print(f"\nO seu IMC é: {imc:.2f}")


#     if imc <18.5:
#      print ("Abaixo do peso")
#     elif imc  <=24.9:
#         print ("Peso normal")
#     else:
#         print ("Acima do peso.")    
#     continu = input("Deseja continuar (s/n): ").lower()
#     if continu == "n":
#        break
#============================================================
            # O que o programa deve fazer:
            # Sortear um número secreto entre 1 e 20.Entrar em um laço de repetição (while) para receber os palpites do usuário.
            # Ler o palpite do usuário (lembre-se de converter para número inteiro usando int()).
             # Comparar o palpite:
            # Se o palpite for menor que o número secreto, exibir: "Muito baixo! Tente um número maior."

            # Se o palpite for maior que o número secreto, exibir: "Muito alto! Tente um número menor."

            # Se o palpite for igual, exibir: "Parabéns! Você acertou!"
            #      e encerrar o jogo (break).


import random

# Sorteia um número inteiro entre 1 e 20 (incluindo o 1 e o 20)
numero_secreto = random.randint(1, 20)
tentativas = 0
while True:
    tentativas = tentativas + 1
    palpite_usuario = int(input("Digite um número: "))
    if palpite_usuario < numero_secreto :
        print("Muito baixo! Tente um número maior.")
    elif palpite_usuario > numero_secreto :
        print ("Muito alto! Tente um número menor.")
    elif palpite_usuario == numero_secreto:
        print(f"  Parabéns! Você acertou! Foram {tentativas} tentativas")
        break    




