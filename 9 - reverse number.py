#Exercise 9:
#Reverse a given number and return true if it is the same as the original number


while True:

  n=int(input('inserisci numero da controllare: '))
  if n==0:
    print('\narrivedOrci!\n')
    break

  def reverse_(n):
    stringa_n=str(n) #rendiamo il numero una stringa per trasformarlo in lista 
    lista_n=list(stringa_n) #una volta diventato lista possiamo rovesciarne gli elementi
    lista_n.reverse()
    ritorno=''.join(lista_n)#il metodo ''.join() permette di tornare 'str'
    n_rovesciato=int(ritorno)
    if n_rovesciato==n:
      print('\nil numero rovesciato è uguale al\'originale:',n_rovesciato,'=',n,'\n')
    else:
      print('\nil numero rovesciato non è uguale all\'originale:',n_rovesciato,'!=',n,'\n')

  reverse_(n)
