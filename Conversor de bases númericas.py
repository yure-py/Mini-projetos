import random


def convert_decimal_to_baseX(base_para_conversão, número):
    copia_do_numero = número 
    resto = []

    while True:
        resto.append(int(número % base_para_conversão))
        print(f'Calculando... {int(número)} / {base_para_conversão}')
        número = número / base_para_conversão
        
        if int(número) == 0:
            break
    print(f'Calculando... {número}')       

    resto.reverse()
    núm_basex = ''.join(map(str, resto))

    print(f'O número ({copia_do_numero})10, é equivalente a ({núm_basex}){base_para_conversão}. \n')


def convert_baseX_to_decimal(base, número):
        
    c = [x for x in range(0,len(str(número)))]
    c.reverse()

    resultados = []
    for idx,value in enumerate(str(número)):
        print(f'calculando... {value}*{base}**{c[idx]}== {(s := int(value)*(base**c[idx]))}')    
        resultados.append(s)
    print(f'O número ({número}){base}, é equivalente a, {sum(resultados)} em decimal \n')    

convert_decimal_to_baseX(5, 879)
convert_baseX_to_decimal(5, 4041)