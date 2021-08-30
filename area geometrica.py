print('\n| Calcolo dell\'area di una figura geometrica scelta |')

while True:
    
    def square(l):
        return l*l

    def rect(b,h):
        return b*h

    def tri(b,h):
        return b*h/2

    def circ(r):
        return (r*r)*3.14

    qwerty=input('\ninserire figura geometrica (quadrato/rettangolo/triangolo/cerchio):\n')
    if '1234567890' in qwerty:
        print('\ninserire una delle figure geometriche indicate tra parentesi\n')
    if qwerty=='quadrato': 
        q=int(input('inserisci lunghezza Lato: '))
        area_q=square(q)
        print('\nl\'area del quadrato è:',area_q,'\n')
    if qwerty=='rettangolo':     
        rb=int(input('inserisci lunghezza Base: '))
        rh=int(input('inserisci lunghezza Altezza: '))
        area_r=rect(rb,rh)
        print('\nl\'area del rettangolo è:',area_r,'\n')
    if qwerty=='triangolo':
        tb=int(input('inserisci lunghezza Base: '))
        th=int(input('inserisci lunghezza Altezza: '))
        area_t=tri(tb,th)
        print('\nl\'area del triangolo è:',area_t,'\n')
    if qwerty=='cerchio':
        rg=int(input('inserisci lunghezza Raggio: '))
        area_ce=circ(rg)
        print('\nl\'area del cerchio è:',area_ce,'\n')
    elif qwerty=='stop':
        break
    else:
        print('\nscelta non valida\n')
    
