class Carta():
    tipo = {1: 'Diamante', 2: 'Trebol', 3: 'Corazon', 4: 'Pica'}

    def __init__(self, valor=1, pinta='Diamante'):
        self.valor = valor
        self.pinta = pinta
        if (valor == 1):
            texto = f'A de {pinta}'
        elif (1 < valor < 11):
            texto = f'{valor} de {pinta}'
        elif (valor == 11):
            texto = f'J de {pinta}'
        elif (valor == 12):
            texto = f'Q de {pinta}'
        elif (valor == 13):
            texto = f'K de {pinta}'
        self.texto = texto

    def __str__(self):
        return f'{self.valor} de {self.pinta}'


class Combinaciones():

    def __init__(self, valor=1, tipo='Par'):
        self.valor = valor
        self.tipo = tipo


def suma_combinaciones(combinaciones):
    peso = {'Par': 4, 'Trio': 10, 'Escalera': 11, 'Color': 12, 'Poker': 15}
    listando = [peso[x.tipo] for x in combinaciones]
    return sum(listando)


def find_combinations(lista):
    listaCombinaciones = []
    listaValores = [carta.valor for carta in lista]
    sinRepetir = list(set(listaValores))
    listaPinta = [carta.pinta for carta in lista]
    setPinta = list(set(listaPinta))

    for numero in sinRepetir:
        if listaValores.count(numero) > 1:

            if listaValores.count(numero) == 2:
                listaCombinaciones.append(Combinaciones(numero, 'Par'))

            elif listaValores.count(numero) == 3:
                listaCombinaciones.append(Combinaciones(numero, 'Trio'))

            elif listaValores.count(numero) == 4:
                listaCombinaciones.append(Combinaciones(numero, 'Poker'))

            elif len(listaValores) == len(sinRepetir):
                listaValores.sort()
                minimo = min(listaValores)
                maximo = max(listaValores)
                if (listaValores == list(range(minimo, maximo + 1))):
                    listaCombinaciones.append(Combinaciones(numero, 'Escalera'))

            elif (len(setPinta) == 1):
                listaCombinaciones.append(Combinaciones(2, 'Color'))
    print(len(setPinta))
    return listaCombinaciones


carta1 = Carta(2, 'Corazon')
carta2 = Carta(6, 'Corazon')
carta3 = Carta(3, 'Corazon')
carta4 = Carta(10, 'Corazon')
carta5 = Carta(9, 'Corazon')
mano = [carta1, carta2, carta3, carta4, carta5]
combinations = find_combinations(mano)
peso = {'Par': 4, 'Trio': 10, 'Escalera': 11, 'Color': 12, 'Poker': 15}
combinaciones_hand = [x.tipo for x in combinations]
print(combinaciones_hand)