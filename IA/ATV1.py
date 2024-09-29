class Node:
    def __init__(self, board, player, move=None, parent=None):
        self.board = board[:]
        self.move = move
        self.player = player
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal1]) or all([spot == letter for spot in diagonal2]):
                return True
        return False

    def get_board(self):
        return ''.join(self.board)


def rotate_90(board):
    return [board[i] for i in [6, 3, 0, 7, 4, 1, 8, 5, 2]]


def rotate_180(board):
    return rotate_90(rotate_90(board))


def rotate_270(board):
    return rotate_90(rotate_180(board))


def mirror(board):
    return [board[i] for i in [2, 1, 0, 5, 4, 3, 8, 7, 6]]


def generate_symmetries(board):
    return [''.join(board), ''.join(rotate_90(board)), ''.join(rotate_180(board)), ''.join(rotate_270(board)), ''.join(mirror(board)),
            ''.join(mirror(rotate_90(board))), ''.join(mirror(rotate_180(board))), ''.join(mirror(rotate_270(board)))]


def is_symmetric(board, seen_boards):
    symmetries = generate_symmetries(board)
    return any(symmetry in seen_boards for symmetry in symmetries)


def build_tree(node, seen_boards, max_depth=9):
    game = TicTacToe()
    game.board = node.board[:]

    if game.current_winner or len(game.available_moves()) == 0 or max_depth == 0:
        print(f"Estado final após jogada {node.move} por {node.player}:")
        game.print_board()
        print("-" * 10)
        return

    seen_boards.add(''.join(node.board))

    for move in game.available_moves():
        game.make_move(move, node.player)
        new_board = game.board[:]

        if is_symmetric(new_board, seen_boards):
            game.board[move] = ' '
            continue

        new_node = Node(new_board, 'O' if node.player == 'X' else 'X', move, parent=node)
        node.add_child(new_node)

        build_tree(new_node, seen_boards, max_depth - 1)
        game.board[move] = ' '


initial_board = [' ' for _ in range(9)]
root = Node(initial_board, 'X')
seen_boards = set()
build_tree(root, seen_boards)
