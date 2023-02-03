def main():
    exemplo1()

def exemplo1():
    dias = ['segunda','terça','quarta','quinta','sexta','sábado','domingo']
    for d in dias:
        if 'sábado' not in d and 'domingo' not in d:
            print(f'{d}-feira')
        else:
            print(d)
    #-----------------
    dias2 = [
        [1,'domingo'],
        [2,'segunda-feira'],
        [3,'terça-feira'],
        [4,'quarta-feira'],
        [5,'quinta-feira'],
        [6,'sexta-feira'],
        [7,'sábado']
        ]

    #d = int(input('Informe o dia da semana, entre: 1 e 7: '))
    d = 1
    if d >= 1 and d <= 7:
        for p in dias2:
            if p[0] == d:
                print(p[1])
    else:
        print('fora do intervalo de dias')
    
    #-----------------
    nums = []
    for i in range(7):  #(exclusivo)    inicia em 0 e inclui 7 valores
        nums.append(i)

    print(nums)

    nums2 = []
    for i in range(1,7):    #(inclusivo, exclusivo)
        nums2.append(i)
    
    print(nums2)

    #-----------------
    alunos = ['Amado','Bispo','Colápso','Dolores','Émilho'] #nomes zuados
    notas = [[8.5, 9.4],
        [8.5, 8.8],
        [7.1, 5.4],
        [7.6, 8.3],
        [9.6, 9.5]]
    resultado = list()
    lista_final = list()
    p = 0

    if len(alunos) == len(notas):
        for a in alunos:
            resultado.append(alunos[a])
            for n in notas[p]:
                soma

            lista_final.append(resultado)
            resultado.clear()
    else:
        print('Quantidade de notas ou alunos está divergente')

    print(lista_final)

main()