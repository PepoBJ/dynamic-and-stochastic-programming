import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'joda', 'queen', 'rey']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(baraja, tamanio_mano):
    mano = random.sample(baraja, tamanio_mano)

    return mano

def ordenar_baraja(baraja):
    baraja_ordenada = []

    for valor in VALORES:
        for carta in baraja:
            if valor == carta[1]:
                baraja_ordenada.append(carta)

    return baraja_ordenada

def main(tamanio_mano, intentos):
    barajas = crear_baraja()

    manos = []

    for _ in range(intentos):
        mano = obtener_mano(barajas, tamanio_mano)
        manos.append(mano)

    escalera = 0

    for mano in manos:
        mano_ordenada = ordenar_baraja(mano)
        mano_ordenada_valores = list(map(lambda x: x[1], mano_ordenada))
        index_valores = VALORES.index(mano_ordenada_valores[0])
        escalera_comparar = VALORES[index_valores:tamanio_mano+index_valores]
        escalera_found = True
        
        # print(escalera_comparar)
        # print(mano_ordenada_valores)

        if len(mano_ordenada_valores) == len(escalera_comparar):
            for i in range(tamanio_mano):
                if mano_ordenada_valores[i] != escalera_comparar[i]:
                    escalera_found = False
                    break
        else:
            escalera_found = False

        if escalera_found:
            escalera += 1

        
    
    probabilidad_escalera = escalera / intentos

    print(f'Probabilidad de que salga una escalera de {tamanio_mano} barajas es {probabilidad_escalera}')

if __name__ == '__main__':
    tamanio_mano = int(input('De cuantas barajas será la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probalidad: '))

    main(tamanio_mano, intentos)