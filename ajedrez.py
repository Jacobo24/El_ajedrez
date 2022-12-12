ajedrez=[   ["♜"   "♞"    "♝"    "♛"	"♚"   "♝"    "♞"    "♜"],
            ["♟"   "♟"    "♟"    "♟"    "♟"    "♟"    "♟"   "♟"],
            ["  "   "  "    "  "    "  "    "  "   "  "   "  "    "  "],
    	    ["  "   "  "    "  "    "  "    "  "   "  "   "  "    "  "],
    	    ["  "   "  "    "  "    "  "    "  "   "  "   "  "    "  "],
            ["  "   "  "    "  "    "  "    "  "   "  "   "  "    "  "],
            ["♙"   "♙"    "♙"    "♙"	"♙"    "♙"   "♙"    "♙"],
            ["♖"   "♘"    "♗"    "♕"	"♔"    "♗"    "♘"   "♖"]]

def imprimir_tablero(ajedrez):
    for i in range(8):
        for j in range(8):
            print(ajedrez[i][j], end=" ")
        print()

def guardar_tablero(nombre, ajedrez):
    nombretxt = "movimientos/" + nombre + ".txt"
    with open (nombretxt, 'a', encoding = 'utf-8') as archivo:
        archivo.writelines('\n')
        for i in range(8):
            archivo.writelines(ajedrez[i])
        archivo.close()

piezas = [  "rn", "dn", "an", "an", "cn", "cn",
            "tn", "tn", "pn", "pn", "pn", "pn",
            "pn", "pn", "pn", "pn",
            "rb", "db", "ab", "ab", "cb", "cb",
            "tb", "tb", "pb", "pb", "pb", "pb",
            "pb", "pb", "pb", "pb", "_"              ]

tablero  = [ "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8",
            "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8",
            "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8",
            "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8",
            "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8",
            "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
            "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8",
            "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8",]

def imprimir_tablero(ajedrez):
    for i in range(8):
        for j in range(8):
            print(ajedrez[i][j], end=" ")
        print()

def juego (ajedrez):
    print (ajedrez)
    print ("¿Qué pieza quieres mover?")
    pieza = input()
    print ("¿A qué posición quieres mover la pieza?")
    posicion = input()
    if pieza in piezas:
        if posicion in tablero:
            print (piezas)
        else:
            print ("La posición no existe")
    else:
        print ("La pieza no existe")
    juego()


def movimiento(ajedrez):
    if tablero[tablero-1] == " ":
        print("No puede mover la ficha a esa posición")
        movimiento(ajedrez)
    elif tablero[tablero-1] != " ":
        ficha = ajedrez[tablero-1]
        tablero_nuevo = input("¿A qué posición quieres mover la ficha? ")
        tablero_nuevo = tablero[tablero_nuevo]
        if ajedrez[tablero_nuevo-1] == " ":
            ajedrez[tablero_nuevo-1] = ficha
            ajedrez[tablero-1] = ' '
            imprimir_tablero(ajedrez)
            juego(ajedrez)
        elif ajedrez[tablero_nuevo] != " ":
            print("No puedes mover ahí")
            movimiento(ajedrez)
        else:
            print("No puedes mover ahí")
            movimiento(ajedrez)
    else:
        print("No puedes mover ahí")
        movimiento(ajedrez)

def principio(ajedrez):
    print("¿Qué quieres hacer?")
    print("Jugar")
    print("Salir")
    opcion = input()
    if opcion == "Jugar":
        juego(ajedrez)
    elif opcion == "Salir":
        print("Hasta luego")
    else:
        print("Opción no válida")

principio(ajedrez)


