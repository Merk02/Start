#Exercise 6:
#Given a list of numbers,
#Iterate it and print only those numbers which are divisible of 5


while True:
  elementi=int(input('\nnumero elementi nella lista: '))
  if elementi==0:
    break
  lista=[]
  for i in range(elementi):
    i=int(input('\ninserisci elemento: '))
    lista.append(i)

  print('\n',lista)

  def divisibili_5(lista):
    lista_divisibili=[]
    for n in lista:
      if n%5==0:
        lista_divisibili.append(n)
    print('gli elementi divisibili per 5 sono:', lista_divisibili,end=' ')
                               

  divisibili_5(lista)
    
