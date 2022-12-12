piezas = [  "rw", "dw", "aw", "aw", "cw", "cw",
            "tw", "tw", "pw", "pw", "pw", "pw",
            "pw", "pw", "pw", "pw",
            "rb", "db", "ab", "ab", "cb", "cb",
            "tb", "tb", "pb", "pb", "pb", "pb",
            "pb", "pb", "pb", "pb", "_"              ]

tablero  = [ "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a",
            "1b", "2b", "3b", "4b", "5b", "6b", "7b", "8b",
            "1c", "2c", "3c", "4c", "5c", "6c", "7c", "8c",
            "1d", "2d", "3d", "4d", "5d", "6d", "7d", "8d",
            "1e", "2e", "3e", "4e", "5e", "6e", "7e", "8e",
            "1f", "2f", "3f", "4f", "5f", "6f", "7f", "8f",
            "1g", "2g", "3g", "4g", "5g", "6g", "7g", "8g",
            "1h", "2h", "3h", "4h", "5h", "6h", "7h", "8h",]

def ajedrez (tablero, piezas):
    tw = "♜"
    cw = "♞"
    aw = "♝"
    rw = "♚"
    dw = "♛"
    rb = "♔"
    db = "♕"
    ab = "♗"
    cb = "♘"
    tb = "♖"
    pw = "♟"
    pb = "♙"
    _ = "  "
    tw = "1a"
    cw = "2a"
    aw = "3a"
    rw = "4a"
    dw = "5a"
    aw = "6a"
    cw = "7a"
    tw = "8a"
    pw = "1b"
    pw = "2b"
    pw = "3b"
    pw = "4b"
    pw = "5b"
    pw = "6b"
    pw = "7b"
    pw = "8b"
    tb = "1h"
    cb = "2h"
    ab = "3h"
    rb = "4h"
    db = "5h"
    ab = "6h"
    cb = "7h"
    tb = "8h"
    pb = "1g"
    pb = "2g"
    pb = "3g"
    pb = "4g"
    pb = "5g"
    pb = "6g"
    pb = "7g"
    pb = "8g"
    _ = "1c"
    _ = "2c"
    _ = "3c"
    _ = "4c"
    _ = "5c"
    _ = "6c"
    _ = "7c"
    _ = "8c"
    _ = "1d"
    _ = "2d"
    _ = "3d"
    _ = "4d"
    _ = "5d"
    _ = "6d"
    _ = "7d"
    _ = "8d"
    _ = "1e"
    _ = "2e"
    _ = "3e"
    _ = "4e"
    _ = "5e"
    _ = "6e"
    _ = "7e"
    _ = "8e"
    _ = "1f"
    _ = "2f"
    _ = "3f"
    _ = "4f"
    _ = "5f"
    _ = "6f"
    _ = "7f"
    _ = "8f"


def mover (tablero, piezas):
    print (tablero)
    print (piezas)
    print ("¿Qué pieza quieres mover?")
    pieza = input()
    print ("¿A qué posición quieres mover la pieza?")
    posicion = input()
    if pieza in piezas:
        if posicion in tablero:
            piezas.remove(pieza)
            piezas.append(posicion)
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
    mover(tablero, piezas)

main()
