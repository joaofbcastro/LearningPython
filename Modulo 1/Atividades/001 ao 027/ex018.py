# Descobre a tangente do angulo inserido pelo usuario.

from math import sin, radians, cos, tan

ângulo = float(input('Digite o valor do angulo: '))
seno = sin(radians(ângulo))
coseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo {} tem como seno {:.2f}.'.format(ângulo, seno))
print('O ângolo {} tem como coseno {:.2f}.'.format(ângulo, coseno))
print('O ângulo {} tem como tangente {:.2f}.'.format(ângulo, tangente))
