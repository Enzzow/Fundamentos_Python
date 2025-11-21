import random 
segredo = random.randint(1,50)

print(" Jogo da adivinhação, teste sua intuição! ")
print(" Você têm 5 tentativas! ( ͡° ͜ʖ ͡°) ")

chances = 5 
tent = 1 # Nº de tentativas

acertou = False #Booleano para verificar se o usuário acertou

while(not acertou and tent<=chances):
  chute = int(input(f"{tent}º tentativa: "))

  if (chute>segredo):
    print(" Errou! O chute foi maior que o segredo!")
    tent+=1
  elif (chute<segredo): 
    print(" Errou! O chute foi menor que o segredo!")
    tent+=1
  else:
    print(f"Parabéns, você acertou depois de {tent} tentativas (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ")
    acertou = True #Interrompe o laço quando o usuário acerta

if(not acertou):
  print(" Você não descobriu o segredo (ಠ_ಠ) ")
  print(f" O segredo era: {segredo} (ʘ ͜ʖ ʘ) ")

print(" Fim do programa! ( ͡~ ͜ʖ ͡°)")

