while True:
    def voc(vo):
        if vo=='a' or vo=='e' or vo=='i' or vo=='o' or vo=='u':
            print('si, <',vo,'> è una vocale')
        elif vo=='0' or vo=='1' or vo=='2' or vo=='3' or vo=='4' or vo=='5' or vo=='6' or vo=='7' or vo=='8' or vo=='9':
            print('<',vo,'> è un numero, inserire un carattere alfabetico')
        else:
            print('no, <',vo,'> è una consonante')
    
    vo=input('inserici carattere: ')
    vo=vo.lower()
    if vo=='stop':
        break
    
    voc(vo)
    
