#Exercise 7:
#Return the count of sub-string “Emma” appears in the given string


while True:
  parola=input('\nche parola vuoi controllare nel testo? ')
  parola=parola.lower()
  if parola=='bast':
    break
  testo=input('inserisci testo in cui controllare: ')

  def contatore_parole(parola, testo):
    print('\nla parola <',parola,'> appare',testo.count(parola),'volta/e nel testo')
    
    
  contatore_parole(parola,testo)
