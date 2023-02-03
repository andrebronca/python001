def main():
    exemplo1()

def exemplo1():
    # exemplos de sintaxe
    b1 = True
    b2 = False
    print(type(b1))
    print(bool(0),', ', bool(1))
    #-------------
    if b1:
        print('Valor T')
    else:
        print('Valor F')
    #----------------
    n = int(input('Informe um número entre 0 e 9: '))
    if n >= 0 and n <= 9:
        print('Número válido: {}'.format(n))
    else:
        print('O valor está fora de 0 a 9: {}'.format(n))
    #----------------
    c = str(input('Informe uma letra: (s/n) '))
    if c == 's' or c == 'n':
        if c == 's':
            print('continua')
        elif c == 'n':  # ou usar o else
            print('pausa')
    else:
        print('opção inválida')

main()