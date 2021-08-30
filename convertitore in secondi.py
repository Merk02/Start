print('--- Convertitore di Giorni, Ore e Minuti in Secondi ---')

while True:
    g=int(input('\ninserisci giorni: '))
    o=int(input('inserisci ore: '))
    m=int(input('inserisci minuti: '))
    def tempo(x,y,z):
        return x*86400+y*3600+z*60

    tempo(g,o,m)
    print(f'\n{g} giorni, {o} ore e {m} minuti sono:', tempo(g,o,m), 'secondi')
        
