temperature: list = [-10, -8, 0, 1, 2, 5, -2, -4]
minimo = temperature[0]
maximo = temperature[0]
for listT in temperature:
    if listT < minimo:
        minimo = listT
    elif listT > maximo:
        maximo = listT
tamanho_temperature = len(temperature)
media = sum(temperature)/tamanho_temperature
print(minimo)
print(maximo)
print(media)