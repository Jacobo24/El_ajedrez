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