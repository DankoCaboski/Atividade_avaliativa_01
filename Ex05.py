oper_h = True
soma_h = 0
primeiro_h =True 

oper_s = False
soma_s = 0
primeiro_s = True

cont_2_em_2 = 1
soma_p = 0

def equacao1(i):
    return (i*2-1)/i

def equacao2(i):
    return i/(i*i) 

def eh_primo(i):
    if i == 2:
        return True
    elif i > 2:
        for n in range(2, i):
            try:
                conta = i % n
                if conta == 0:
                    return False            
            except:
                pass 
        
        return True
    else: 
        return False 

num = int(input('Informe um número maior ou igual a 50: '))
if num >= 50:
    for i in range(1,num+1):

        if oper_h or primeiro_h:
            soma_h+=equacao1(i)
            if not primeiro_h:
                oper_h = False
            primeiro_h = False

        else:
            soma_h-=equacao1(i)
            oper_h = True
        
        if primeiro_s:
            soma_s += equacao2(i)
            primeiro_s = False

        else:
            if oper_s:
                soma_s += equacao2(i)
                oper_s = False 
            
            else:
                soma_s -= equacao2(i)
                oper_s = True
        
        if eh_primo(i):
            soma_p += i/(cont_2_em_2**3)
            cont_2_em_2 += 2

    print(f'H = {soma_h}')
    print(f'S = {soma_s}')
    print(f'P = {soma_p}')
else:
    print(f'{num} é um número invalido')