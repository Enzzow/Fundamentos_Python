estoque = ["Maça","Uva","Banana","Abacaxi"]
fruta = input(" Informe a fruta que deseja encontrar no estoque: ")
fruta = unidecode.unidecode(fruta).title()

if fruta in estoque:
  print(" Em estoque...")
else:
  print(" Fora de estoque.")
