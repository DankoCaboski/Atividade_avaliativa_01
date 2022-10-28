maior_soma=0 
soma=0
ultimo=-1
maior_sequencia=0
sequencia=0

maior_seq_const = 0
seq_const = 0
maior_num_seq = 0
num_seq = 0


def Validar_sequencia():
    global sequencia, maior_sequencia, soma, maior_soma  
    if sequencia > maior_sequencia:
        maior_sequencia = sequencia
        maior_soma = soma 

    elif sequencia == maior_sequencia:
        if soma > maior_soma:
            maior_sequencia = sequencia
            maior_soma = soma


def Validar_sequencia_const():
    global seq_const, maior_seq_const, num_seq, maior_num_seq  
    if seq_const > maior_seq_const:
        maior_seq_const = seq_const
        maior_num_seq = num_seq 

    elif seq_const == maior_seq_const:
        if num_seq > maior_num_seq:
            maior_seq_const = seq_const
            maior_num_seq = num_seq 


for a in range(150):
    num = int(input('Numero:  '))
    if ultimo+1 == num:
        soma += num 
        sequencia +=1 
    
    else:
        Validar_sequencia()
            
        sequencia = 1
        soma = num 
    
    if ultimo == num:
        seq_const += 1 
        num_seq = ultimo 
    
    else:
        Validar_sequencia_const()
        seq_const = 1
        num_seq = num 

    ultimo = num

Validar_sequencia()
Validar_sequencia_const()

print(f'A maior sequencia possui {maior_sequencia} elementos e sua e soma {maior_soma}')
print(f'A maior sequencia constante possui {maior_seq_const} vezes o numero {maior_num_seq}')


