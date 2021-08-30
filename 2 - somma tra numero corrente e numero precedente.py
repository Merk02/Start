#Exercise 2:
#Given a range of the first 10 numbers,
#Iterate from the start number to the end number,
#and In each iteration print the sum of the current number and previous number

while True:
  def fun(numero):
    n_precedente=0
    for i in range(numero):
      somma = n_precedente + i
      print('il numero di partenza è',n_precedente,'il numero corrente è',i,'la somma è',somma)
      n_precedente=i

  numero=int(input('inserire il range: '))
  fun(numero)

  if numero==0:
    break
