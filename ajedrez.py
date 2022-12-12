ajedrez=[   ["♜"   "♞"    "♝"    "♛"	"♚"   "♝"    "♞"    "♜"],
            ["♟"   "♟"    "  "    "♟"    "♟"    "♟"    "♟"   "♟"],
            ["  "   "  "    "  "    "  "    "  "   "  "   "  "    "  "],
    	    ["  "   "  "    "♟"    "  "    "  "   "  "   "  "    "  "],
    	    ["  "   "  "    "  "    "  "    "  "   "  "   "♙"    "  "],
            ["  "   "  "    "  "    "  "    "  "   "  "   "  "    "  "],
            ["♙"   "♙"    "♙"    "♙"	"♙"    "♙"   "  "    "♙"],
            ["♖"   "♘"    "♗"    "♕"	"♔"    "♗"    "♘"   "♖"]]

# Para que se vea el tablero de ajedrez
def imprimir_tablero(ajedrez):
    for i in range(8):
        for j in range(8):
            print(ajedrez[i][j], end=" ")
        print()

# Para que puedas mover las piezas
def mover_pieza(ajedrez, pieza, fila, columna):
    for i in range(8):
        for j in range(8):
            if ajedrez[i][j] == pieza:
                ajedrez[i][j] = "  "
                ajedrez[fila][columna] = pieza
                return