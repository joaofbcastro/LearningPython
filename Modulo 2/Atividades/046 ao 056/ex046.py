# Contagem regressiva

from time import sleep

print('Queima de fogos em:')
sleep(1)
for c in range(10, -1, -1):
    print("{:2}".format(c))
    sleep(1)
print('Boom!! Bom! Pow!')
