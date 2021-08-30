print('\n--- Controlla se il testo inserito è uguale al contrario ---')

while True:
    def fun(s):
        if s[:]==s[::-1]:
            print(f'\nsi, < {s} > è un palindromo')
        else:
            print(f'\nno, < {s} > non è un palindromo')
    a=input('\ninserire testo: ')
    if a=='stop':
        break
    fun(a)
    
            
