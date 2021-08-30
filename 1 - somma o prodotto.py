#Exercise 1:
#Given two integer numbers return their product.
#If the product is greater than 1000, then return their sum
while True:
  a=int(input('primo nummero: '))
  b=int(input('secondo nummero: '))
  def somma_o_prodotto(a,b):
    if a*b<1000:
      print('\na * b = ', a*b,'\n')
    else:
      print('\nqui il prodotto di a e b è superiore a 1000...\npertanto a + b =',a+b, '\n')

  
  somma_o_prodotto(a,b)
