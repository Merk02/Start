#Exercise 12:
#Calculate income tax for the given income by adhering to the below rules

print('\n--- Calcolatore tasse ---')

while True:
    inp=int(input('\n\ninserire ammontare introiti: '+'euro '))
    if inp==0:
        break
    print(f'\nl\'ammontare è pari a {inp} euro\n')
    
    def tasse(num):
        if num<=10000:
            print('\nl\'ammontare della tassa è relativa a euro',num*0/100)
        elif 10000<num<=20000:
            print(f'\nl\'ammontare della tassa è relativa a euro',(num-10000)*10/100)
        elif num>20000:
            print('\nl\'ammontare della tassa è relativa a euro',(num-10000)*10/100+(num-20000)*20/100)

    tasse(inp)

