# Converte metro em centimetros e milimetros.
medida = float(input('Digite quantos metros: '))
centimetros = medida * 100
milimetros = medida * 1000
print('A medida de {}m corresponde à {}cm e {}mm.'.format(medida, int(centimetros), int(milimetros)))