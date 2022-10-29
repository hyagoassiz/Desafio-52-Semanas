try:

    valor_inicial = float(input('Digite o valor que você gostaria de começar a guardar: '))
    semana = 0
    aportes = 0
    consolidado = []

    for i in range(52):
        semana += 1
        aportes += valor_inicial
        consolidado.append(aportes)
        print('Na Semana {} Deposite R$ {:.2f}'.format(semana, aportes))

    print('Ao final do Desafio você terá: R$ {:.2f}'.format(sum(consolidado)))


except:
    print('Erro! Digite apenas números. Exemplo: se quiser simular com R$ 1.00 digite: 1.00')

