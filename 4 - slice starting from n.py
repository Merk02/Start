#Exercise 4:
#Given a string and an integer number n,
#remove characters from a string starting from zero up to n and return a new string

while True:

  parola=input('parola da tagliare: ')
  parola=parola.lower()
  if parola=='bast':
    break
  numero=int(input('numero indice di partenza: '))

  
  def cut(parola, numero):
    return parola[numero:]

  print(cut(parola, numero))
