print('\n--- Convertitore di Metri in Miglia, iarde, Piedi, Pollici ---')

while True:
    w=int(input('\ninserire metri: '))
    def mt_ml(k):
        return round(k*0.000621371, 4)
    def mt_y(j):
        return round(j*1.09361, 4)
    def mt_f(p):
        return round(p*3.281, 4)
    def mt_i(i):
        return round(i*39.37, 4)

    miglia=mt_ml(w)
    yard=mt_y(w)
    feet=mt_f(w)
    inches=mt_i(w)
    print(f'\n{w} metri sono: ', miglia, 'miglia, ', yard, 'iarde, ', feet, 'piedi, ', inches, 'pollici')

