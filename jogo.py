from random import randint
numero = randint(0,9)
nome = input("Digite o seu nome: ")
n = int(input("Oi " + nome.upper() + ", eu sou Goku!" + "\n"
          + "E agora vamos testar o seu QI e conhecer o seu poder de Cavaleiro Z." + "\n"
          + "Me diga, qual o número eu pensei (de 0 à 9): "))
contador = 3

while numero!=n:

    contador = contador - 1

    if contador > 0:

        if n>numero:
            n = int(input("\n" + "Você digitou um número maior" + "\n"
                      + "Você ainda tem " + str(contador) + " tentativas" + " Tente novamente: "))
        else:
            n = int(input("\n" + "Você digitou um número menor" + "\n"
                          + "Você ainda tem " + str(contador) + " tentativas" + " Tente novamente: "))
    else:
        print("GAME OVER")
        print("Eu pensei no número " + str(numero))
        break

if numero == n:
    print(numero, n)
    print(nome.upper(),  " PARABÉNS, AGORA VOCÊ É UM CAVALEIRO Z")