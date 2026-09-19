import random

pontoUsuario = 0
pontoMaquina = 0

print("JOKENPO - O JOGO")
print("----------------")
print()
resp = int(input("""Deseja jogar?
[1] sim
[0] não\n"""))
print()
if resp != 1 or 0:
  print("Opção invalida. Informe uma das opções acima..")
print()
while resp != 0:
  jogador1 = int (input("""Digite um numero de 1 a 3 sendo eles:
[1]Papel
[2]Tesoura
[3]Pedra\n"""))
  jogador2 = random.randint(1,3)
  match jogador1:
    case 1: 
     if jogador1 == 1 and jogador2 == 3:
       print("O Usuario foi o vencedor!")
       pontoUsuario += 1
       print(f"""Pontuação:
Você: {pontoUsuario}
Computador: {pontoMaquina}""")
     elif jogador1 == 1 and jogador2 == 2:
       print("O computador foi o vencedor!")
       pontoMaquina += 1
       print(f"""Pontuação:
Você: {pontoUsuario}
Computador: {pontoMaquina}""")
     else:
       print("O jogo deu empate!")
       print(f"""Pontuação:
Você: {pontoUsuario}
Computador: {pontoMaquina}""")
    case 2:
      if jogador1 == 2 and jogador2 == 1:
       print("O Usuario foi o vencedor!")
       pontoUsuario += 1
       print(f"""Pontuação:
Você: {pontoUsuario}
Computador: {pontoMaquina}""")
      elif jogador1 == 2 and jogador2 == 3:
       print("O computador foi o vencedor!")
       pontoMaquina += 1
       print(f"""Pontuação:
Você: {pontoUsuario}
Computador: {pontoMaquina}""")
      else:
       print("O jogo deu empate!")
       print(f"""Pontuação:
Você: {pontoUsuario}
Computador: {pontoMaquina}""")
    case 3:
      if jogador1 == 3 and jogador2 == 2:
         print("O Usuario foi o vencedor!")
         pontoUsuario += 1
         print(f"""Pontuação:
Você: {pontoUsuario}
Computador: {pontoMaquina}""")
      elif jogador1 == 3 and jogador2 ==1:
         print("O computador foi o vencedor!")
         pontoMaquina += 1
         print(f"""Pontuação:
Você: {pontoUsuario}
Computador: {pontoMaquina}""")
      else:
         print("O jogo deu empate!")
         print(f"""Pontuação:
Você: {pontoUsuario}
Computador: {pontoMaquina}""")
    case _:
      print("Opção de escolha inválida! Digite uma das opções acima.")
  resp = int (input("""Deseja continuar jogando?
  [1] sim
  [0] não\n"""))
print()
print("PONTUAÇÃO FINAL")
print("---------------")
print(f"você: {pontoUsuario}")
print(f"Computador: {pontoMaquina}")
print()
if pontoUsuario>pontoMaquina:
  print("Você foi o grande vencedor da competição!")
else:
  print("O computador foi o grande vencedor da competição!")
