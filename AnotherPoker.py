class Carta():
    tipo = {1: 'Diamante', 2: 'Trebol', 3: 'Corazon', 4: 'Pica'}

    def __init__(self, valor=1, pinta='Diamante'):
        self.valor = valor
        self.pinta = pinta
        texto = ''
        if (valor == 14):
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

    def __str__(self):
        return f'{self.tipo} de {self.valor}'


def find_combinations(lista):
    listaCombinaciones = []
    listaValores = [carta.valor for carta in lista]
    sinRepetir = list(set(listaValores))
    listaPinta = [carta.pinta for carta in lista]
    setPinta = list(set(listaPinta))

    for numero in sinRepetir:
        if len(sinRepetir) <= 4:
            if listaValores.count(numero) > 1:

                if listaValores.count(numero) == 2:
                    listaCombinaciones.append(Combinaciones(numero, 'Par'))

                elif listaValores.count(numero) == 3:
                    listaCombinaciones.append(Combinaciones(numero, 'Trio'))

                elif listaValores.count(numero) == 4:
                    listaCombinaciones.append(Combinaciones(numero, 'Poker'))

    if (len(listaCombinaciones) == 2):
        fullHouse = [combinacion.tipo for combinacion in listaCombinaciones]
        fullHval = [combinacion.valor for combinacion in listaCombinaciones]
        if ('Trio' in fullHouse) and ('Par' in fullHouse):
            high_index = fullHouse.index('Trio')
            high = fullHval[high_index]
            listaCombinaciones.clear()
            listaCombinaciones.append(Combinaciones(high, 'Full House'))

        else:
            high = max(fullHval)
            listaCombinaciones.clear()
            listaCombinaciones.append(Combinaciones(high, 'Double Pair'))

    if len(listaValores) == len(sinRepetir):
        listaValores.sort()
        minimo = min(listaValores)
        maximo = max(listaValores)
        if (listaValores == list(range(minimo, maximo + 1))):
            listaCombinaciones.append(Combinaciones(maximo, 'Escalera'))

        elif (1 in listaValores):
            listaCombinaciones.append(Combinaciones(14, 'HighCard'))

        else:
            listaCombinaciones.append(Combinaciones(max(listaValores), 'HighCard'))

    if (len(setPinta) == 1):
        if (len(listaCombinaciones) == 0):
            listaCombinaciones.append(Combinaciones(2, 'Color'))
        elif listaCombinaciones[0].tipo == 'Escalera':
            listaCombinaciones.append(Combinaciones(2, 'Color'))

    fullHouse = [combinacion.tipo for combinacion in listaCombinaciones]

    if ('Color' in fullHouse and 'Escalera' in fullHouse):
        listaCombinaciones.clear()
        listaCombinaciones.append(Combinaciones(2, 'Escalera Real Imperial'))

    output = listaCombinaciones.pop()
    # print(len(setPinta))
    return output
def mejorCombinacion(cartasMesa,cartasJugador):
    peso = {'HighCard': 1, 'Par': 4, 'Double Pair': 8, 'Trio': 10, 'Escalera': 11, 'Color': 12, 'High Card': 14,
            'Poker': 15, 'Escalera Real Imperial': 18}

    permutacion = [(0, 1, 2), (0, 1, 3), (0, 1, 4), (1, 2, 3), (1, 2, 4), (2, 3, 4)]
    for comb in permutacion:
        acumulado = 0
        combMesa = [cartasMesa[comb[0]], cartasMesa[comb[1]], cartasMesa[comb[2]]]
        cartasTotal = cartasJugador + combMesa
        combinacion = find_combinations(cartasTotal)
        sumaComb = combinacion.valor * peso[combinacion.tipo]
        if sumaComb > acumulado:
            acumulado = sumaComb
            indice = permutacion.index(comb)

    final = permutacion[indice]
    bestHand = cartasJugador + [cartasMesa[final[0]], cartasMesa[final[1]], cartasMesa[final[2]]]
    bestComb = find_combinations(bestHand)
    return bestComb

cartasMesa = [Carta(2, 'Corazon'), Carta(3, 'Corazon'), Carta(9, 'Pica'), Carta(5, 'Corazon'), Carta(8, 'Corazon')]
cartasJugador = [Carta(2, 'Corazon'), Carta(8, 'Corazon')]
combinacion=mejorCombinacion(cartasMesa,cartasJugador)
print(combinacion)
