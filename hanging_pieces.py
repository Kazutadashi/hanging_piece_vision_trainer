class ChessBoard:
    def __init__(self):
        self.current_board_fen = "8/8/8/8/8/8/8/8 w - - 0 1"
        self.squares = {
                        "a8": None, "b8": None, "c8": None, "d8": None, "e8": None, "f8": None, "g8": None, "h8": None,
                        "a7": None, "b7": None, "c7": None, "d7": None, "e7": None, "f7": None, "g7": None, "h7": None,
                        "a6": None, "b6": None, "c6": None, "d6": None, "e6": None, "f6": None, "g6": None, "h6": None,
                        "a5": None, "b5": None, "c5": None, "d5": None, "e5": None, "f5": None, "g5": None, "h5": None,
                        "a4": None, "b4": None, "c4": None, "d4": None, "e4": None, "f4": None, "g4": None, "h4": None,
                        "a3": None, "b3": None, "c3": None, "d3": None, "e3": None, "f3": None, "g3": None, "h3": None,
                        "a2": None, "b2": None, "c2": None, "d2": None, "e2": None, "f2": None, "g2": None, "h2": None,
                        "a1": None, "b1": None, "c1": None, "d1": None, "e1": None, "f1": None, "g1": None, "h1": None,
                        }

    def set_board_fen(self, fen):
        self.current_board_fen = fen

    def get_board_fen(self):
        return self.current_board_fen

    def set_squares(self):
        """
        Goes through the FEN that is currently set and then sets the piece type for each square
        :return:
        """

        # we split the FEN so we can go row by row
        split_fen = self.current_board_fen.split('/')

        # to maintain the human-readability of the board, we use an ascii and standard
        # representation of the current square
        current_square_ascii = [ord('a'), 8]
        current_square = 'a8'

        # go over ever row of the FEN, and then every square within that row to determine how to
        # set the board state
        for row in split_fen:
            for square in row:
                # if the square is a space we are done with the board setup phase and can stop
                if square == ' ':
                    return
                if square.isnumeric():
                    # if the FEN gives us a number it means we need to have this many blank squares
                    # on that row starting from the top left
                    for i in range(int(square)):
                        self.squares[current_square] = None
                        # move one square to the right after we set it to none
                        current_square_ascii[0] += 1
                        current_square = chr(current_square_ascii[0]) + str(current_square_ascii[1])
                else:
                    # convert the square back into human-readable format
                    self.squares[current_square] = square
                    current_square_ascii[0] += 1
                    current_square = chr(current_square_ascii[0]) + str(current_square_ascii[1])
            # after we go to a new row, change the current squares row by -1 since we
            # are going top to bottom
            current_square_ascii[1] -= 1
            current_square_ascii[0] = ord('a')
            current_square = chr(current_square_ascii[0]) + str(current_square_ascii[1])

    def get_squares(self):
        return self.squares


FEN = "2rk3r/pppbb2p/n2qpp1n/3p2p1/QP2P3/N1P2P2/PB1PK1PP/R1N2BR1 w - - 4 12"
