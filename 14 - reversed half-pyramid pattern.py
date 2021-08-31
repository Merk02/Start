#Exercise 14:
#Print downward Half-Pyramid Pattern with Star (asterisk)

print('\n--- piramide inversa ---')

while True:
    inp=int(input('\n\ninserire numero degli asterischi: '))
    if inp==0:
        break
    def pyramid(x):
        for i in range(x,0,-1):
            for j in range(0,i-1):
                print('*',end=' ')
            print('')
    pyramid(inp)
