ajedrez=[   ["♜"   "♞"    "♝"    "♛"	"♚"   "♝"    "♞"    "♜"],
            ["♟"   "♟"    "  "    "♟"    "♟"    "♟"    "♟"   "♟"],
            ["  "   "  "    "  "    "  "    "  "   "  "   "  "    "  "],
    	    ["  "   "  "    "♟"    "  "    "  "   "  "   "  "    "  "],
    	    ["  "   "  "    "  "    "  "    "  "   "  "   "♙"    "  "],
            ["  "   "  "    "  "    "  "    "  "   "  "   "  "    "  "],
            ["♙"   "♙"    "♙"    "♙"	"♙"    "♙"   "  "    "♙"],
            ["♖"   "♘"    "♗"    "♕"	"♔"    "♗"    "♘"   "♖"]]

def imprimir_tablero(ajedrez):
    for i in range(8):
        for j in range(8):
            print(ajedrez[i][j], end=" ")
        print()

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

def ajedrez (tablero, piezas):
    tn = "♜"
    cn = "♞"
    an = "♝"
    rn = "♚"
    dn = "♛"
    rb = "♔"
    db = "♕"
    ab = "♗"
    cb = "♘"
    tb = "♖"
    pn = "♟"
    pb = "♙"
    _ = "  "
    tn = "a1"
    cn = "a2"
    an = "a3"
    rn = "a4"
    dn = "a5"
    an = "a6"
    cn = "a7"
    tn = "a8"
    pn = "b1"
    pn = "b2"
    pn = "b3"
    pn = "b4"
    pn = "b5"
    pn = "b6"
    pn = "b7"
    pn = "b8"
    tb = "h1"
    cb = "h2"
    ab = "h3"
    rb = "h4"
    db = "h5"
    ab = "h6"
    cb = "h7"
    tb = "h8"
    pb = "g1"
    pb = "g2"
    pb = "g3"
    pb = "g4"
    pb = "g5"
    pb = "g6"
    pb = "g7"
    pb = "g8"
    _ = "c1"
    _ = "c2"
    _ = "c3"
    _ = "c4"
    _ = "c5"
    _ = "c6"
    _ = "c7"
    _ = "c8"
    _ = "d1"
    _ = "d2"
    _ = "d3"
    _ = "d4"
    _ = "d5"
    _ = "d6"
    _ = "d7"
    _ = "d8"
    _ = "e1"
    _ = "e2"
    _ = "e3"
    _ = "e4"
    _ = "e5"
    _ = "e6"
    _ = "e7"
    _ = "e8"
    _ = "f1"
    _ = "f2"
    _ = "f3"
    _ = "f4"
    _ = "f5"
    _ = "f6"
    _ = "f7"
    _ = "f8"


def mover (tablero, piezas, ajedrez):
    print (tablero)
    print (piezas)
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

def imprimir_tablero (tablero, piezas):
    print (tablero)
    print (piezas)

def main ():
    ajedrez(tablero, piezas)
    imprimir_tablero(tablero, piezas)
    mover(tablero, piezas, ajedrez)

main()
