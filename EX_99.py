def maior(*n):
    print('-=' * (len(n) * 7))
    print(f'Os números que você informou foram {n} e no total foram {len(n)} número informados')
    print(f'E o maior número informado foi {max(n)}')
    print('-=' * (len(n) * 7))


maior(14, 10, 7, 92, 124, 25, 56, 39, 50, 1)
maior(14, 10, 7, 92, 20, 29, 900)

