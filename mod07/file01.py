
def main(s,n):
    i = int(input('Informe um número: '))
    f = 3.1415
    s = n
    s += i
    print("texto: ",s, ', número: ',float(n),', tipos: ',type(s),type(n))
    print("msg: {}, número inf.: {}, parâmetro: {}, soma: {}".format(s,i,n,s))
    print(f'parametros: string: {s}, número: {n}. input: {i}. soma: {s}')
    print('{:.2f}'.format(f), ' {:.1f}'.format(f),' {:.0f}'.format(f))
    print(f'{f:.2f}')

main('oi',3)