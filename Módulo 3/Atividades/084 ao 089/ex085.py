números = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        números[0].append(num)
    elif num % 2 == 1:
        números[1].append(num)
print(
    "="*45,
    f'\nOs números Pares digitados foram: {sorted(números[0])}',
    f'\nOs valores impares digitados foram: {sorted(números[1])}'
)
