def main():
    lista1(10,11,12,13) #parametros
    lista2()
    lista3()
    lista4()
    lista5()
    lista6()
    lista7()

def lista1(a,b,c,d):
    soma = a + b + c + d
    print(f'soma: {soma:.2f}')

def lista2():
    l_str = ['a','b','c','d']
    l_str.append('e')
    l_str.append('f')
    print(l_str)
    print(l_str[0])

def lista3():
    nomes = []
    mista = list(['a','hoje',1,2,2023])
    print(mista)

def lista4():
    l1 = [1,2,3]
    l2 = l1 #passagem por referência, apontam para a mesma lista, mudar l2 irá mudar l1
    l2.append(4)
    l2.append(6)
    print(l2)
    l3 = l1[:]  #pega todos os elementos e adiciona em l3, clonagem
    l3.append('a')
    print(l3, l1)
    print(l3[1:3]) #[3] nesse caso fica de fora. [1] nesse caso fica incluso
    print(l3[2:])
    print(l3[:4]) #[4] nesse caso fica de fora
    print(l3[:])
    # [ a partir (incluso) até (:) este (excluído)]

def lista5():
    l1 = [1,3,5]
    l2 = [2,4,6]
    l3 = l1 + l2
    print(l3)

def lista6():
    l1 = list()
    l1.append(2)
    l1.append(1)    #adiciona sempre no final
    l1.append('nome')
    print(l1)
    id_n = l1.index('nome') #retorna o índice do elemento no parametro
    print(id_n)
    l1.insert(1,'sobrenome')    #insere na posição [1]
    print(l1)
    print(5 in l1)
    print('oi' in l1)
    print(2 in l1)
    l1.remove('nome') #se não estiver na lista, ocorre erro
    print(l1)
    l1.pop()    #remove o último elemento
    print(l1)
    l1.append([3,5,7,8])
    l1 += [9,0,1,12,20,14,5]
    print(l1)
    l1.pop(2)   #remove o elemento da posição [2]
    print(l1)
    del(l1[1])  #remove o elemento
    print(l1)
    l1.sort()   #ordenar a lista, sort() não retorna nada
    print(l1)
    print(sorted([3,1,4,7,2,0]))    #função de ordenação do python, sorted retorna uma lista ordenada

def lista7():
    nome = 'python revisando 2023'
    nome2 = nome[ :nome.index(' ')] +'_'+ nome[(nome.index(' ') + 1):]
    print(nome)
    print(nome[1])
    print(nome2)
    print(nome[-1:])
    print('b' in nome)
    print('b' not in nome)
    s1 = 'PYTHON'
    print(s1.lower())   #para minúsculo
    print(len(s1))  #tamanho da string
    print( nome.isalpha())
    print( nome2.isalpha())
    print( s1.isalpha())    # só contém letras
    print( '*¨@%'.isalpha())
    s2 = '    com espaços   '
    print(s2)
    print(s2.strip())   #remove os espaços
    s3 = ','.join(s1)
    print( s3 )
    s4 = s3.split(',')
    print(s4)


main()

