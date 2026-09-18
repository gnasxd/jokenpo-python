import random

print("JOKENPO - O JOGO")
print("----------------")
resp = ("""Deseja jogar?
[1] sim
[0] não/n""")

while resp != 0:
  jogador1 = int ("""Digite um numero de 1 a 3 sendo eles:
[1]Papel
[2]Tesoura
[3]Pedra\n""")
  jogador2 = random.randint(1,3)

  match jogador1:
    case 1: 
     if jogador1 == 1 and jogador2 == 3:
       print("O Usuario foi o vencedor!")
     elif jogador1 == 1 and jogador2 == 2:
       print("O computador foi o vencedor!")
     else:
       print("O jogo deu empate!")
    case 2:
      if jogador1 == 2 and jogador2 == 1:
       print("O Usuario foi o vencedor!")
      elif jogador1 == 2 and jogador2 == 3:
       print("O computador foi o vencedor!")
      else:
       print("O jogo deu empate!")
    case 3:
      if jogador1 == 3 and jogador2 == 2:
         print("O Usuario foi o vencedor!")
      elif jogador1 == 3 and jogador2 ==1:
         print("O computador foi o vencedor!")
      else:
         print("O jogo deu empate!")
    case _:
      print("Opção de escolha inválida! Digite uma das opções acima.")