#Exercise 3:
#Given a string,
#display only those characters which are present at an even index number.

while True:
  parola=input('\ninserire parola di cui prendere l\'indice pari: ')

  if parola=='bast':
    break

  def even_str(parola):
    return list(parola[::2])

  print(even_str(parola))

