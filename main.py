while True:
    print(f'{"TABUADA":^40}')
    print(f'{"="*14:-^40}')
    n = int(input('Digite um número (negativos para parar): '))
    if n < 0:
        break
    print('~'*40)
    for c in range(1, 11):
        print(f'{n} X {c:2} = {c*n}')
    print('~'*40)
print('Programa Finalizado')
