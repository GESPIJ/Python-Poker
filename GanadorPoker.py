from random import randint


class Carta():
    tipo = {1: 'Diamante', 2: 'Trebol', 3: 'Corazon', 4: 'Pica'}

    def __init__(self, valor=1, pinta='Diamante'):
        self.valor = valor
        self.pinta = pinta
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
        self.texto=f'{self.tipo} de {self.valor}'

    def __str__(self):
        return f'{self.tipo} de {self.valor}'


def suma_combinaciones(combinaciones):
    peso = {'HighCard': 1, 'Par': 4, 'Double Pair': 8, 'Trio': 10, 'Escalera': 11, 'Color': 12, 'High Card': 14,
            'Poker': 15,
            'Escalera Real Imperial': 18}
    listando = [peso[x.tipo] for x in combinaciones]
    return sum(listando)


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


def generate_hand(n):
    mano = []
    tipo = {1: 'Diamante', 2: 'Trebol', 3: 'Corazon', 4: 'Pica'}
    for x in range(0, n):
        carta = Carta(randint(2, 14), tipo[randint(1, 4)])
        mano.append(carta)
    return mano


def winner_combination(*jugadores):
    peso = {'HighCard': 1, 'Par': 4, 'Double Pair': 8, 'Trio': 10, 'Escalera': 11, 'Color': 12, 'High Card': 14, 'Full House': 15,
            'Poker': 16, 'Escalera Real Imperial': 18}
    suma = [1] * len(jugadores)

    for indice,jugador in enumerate(jugadores):
        suma[indice] = peso[jugador.tipo]

    maximo = max(suma)
    ind_winner = suma.index(maximo)
    veces=suma.count(maximo)
    tipoEmpate=jugadores[ind_winner].tipo

    if (veces > 1):
       # listaDesempate=[(indice,peso[jugador.tipo]*jugador.valor) for indice,jugador in
                        #enumerate(jugadores) if (jugador.tipo==tipoEmpate)]
        listaindices=[jugadores.index(jugador) for jugador in jugadores if jugador.tipo==tipoEmpate]
        listaValores=[peso[jugador.tipo]*jugador.valor for jugador in jugadores if jugador.tipo==tipoEmpate]
        maximo=max(listaValores)
        ind_winner=listaindices[listaValores.index(maximo)]
        if listaValores.count(maximo)>1:
            ind_winner=-2
    ind_winner=ind_winner+1
    return ind_winner

def mejorCombinacion(cartasMesa,cartasJugador):
    peso = {'HighCard': 1, 'Par': 4, 'Double Pair': 8, 'Trio': 10, 'Escalera': 11, 'Color': 12, 'Full House':14,
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


hand1 = generate_hand(2)
hand2 = generate_hand(2)
hand3= generate_hand(2)
cartasMesa=generate_hand(5)
handTexto1 = [carta.texto for carta in hand1]
handTexto2 = [carta.texto for carta in hand2]
handTexto3 = [carta.texto for carta in hand3]
cartasMesaTexto = [carta.texto for carta in cartasMesa]

print(handTexto1)
print(handTexto2)
print(handTexto3)
print(cartasMesaTexto)

#hand1=[Carta(2,'Diamante'), Carta(3,'Trebol'), Carta(4,'Diamante'), Carta(5,'Pica'), Carta(13,'Trebol')]
#hand2=[Carta(3,'Pica'), Carta(9,'Pica'), Carta(2,'Diamante'), Carta(4,'Corazon'), Carta(13,'Diamante')]
#hand3=[Carta(2,'Pica'), Carta(9,'Pica'), Carta(5,'Diamante'), Carta(4,'Corazon'), Carta(10,'Diamante')]
combinations1 = mejorCombinacion(cartasMesa,hand1)
print(combinations1)
combinations2 = mejorCombinacion(cartasMesa,hand2)
print(combinations2)
combinations3 = mejorCombinacion(cartasMesa,hand3)
print(combinations3)
winner=winner_combination(combinations1,combinations2,combinations3)
print(f'Gano el jugador {winner}')



