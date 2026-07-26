import random
import json


def generar_carton():

    columnas = [
        sorted(random.sample(range(1, 16), 5)),
        sorted(random.sample(range(16, 31), 5)),
        sorted(random.sample(range(31, 46), 5)),
        sorted(random.sample(range(46, 61), 5)),
        sorted(random.sample(range(61, 76), 5)),
    ]

    columnas[2][2] = "FREE"

    carton = []

    for i in range(5):
        carton.append([
            columnas[0][i],
            columnas[1][i],
            columnas[2][i],
            columnas[3][i],
            columnas[4][i]
        ])

    return json.dumps(carton)


def leer_carton(texto):
    return json.loads(texto)


def sacar_numero(partida):

    from .models import NumeroSorteado

    numeros_salidos = list(
        NumeroSorteado.objects.filter(partida=partida)
        .values_list("numero", flat=True)
    )

    disponibles = [n for n in range(1, 76) if n not in numeros_salidos]

    if not disponibles:
        return None

    numero = random.choice(disponibles)

    NumeroSorteado.objects.create(
        partida=partida,
        numero=numero
    )

    return numero


def verificar_bingo(carton, numeros):

    # ---------- FILAS ----------

    for fila in carton:

        correcta = True

        for numero in fila:

            if numero == "FREE":
                continue

            if numero not in numeros:
                correcta = False

        if correcta:
            return True


    # ---------- COLUMNAS ----------

    for c in range(5):

        correcta = True

        for f in range(5):

            numero = carton[f][c]

            if numero == "FREE":
                continue

            if numero not in numeros:
                correcta = False

        if correcta:
            return True


    # ---------- DIAGONAL PRINCIPAL ----------

    correcta = True

    for i in range(5):

        numero = carton[i][i]

        if numero == "FREE":
            continue

        if numero not in numeros:
            correcta = False

    if correcta:
        return True


    # ---------- DIAGONAL SECUNDARIA ----------

    correcta = True

    for i in range(5):

        numero = carton[i][4-i]

        if numero == "FREE":
            continue

        if numero not in numeros:
            correcta = False

    if correcta:
        return True

    return False