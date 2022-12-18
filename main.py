class Board:
    def __init__(self):
        self.board = [['-'] * 3 for i in range(3)]
        self.winner = '-'
        self.n = 0
        self.move = 'x'
        self.moveX = True

    def setCoordsThroughInput(self):
        if self.moveX:
            self.move = 'x'
            print('x')
        else:
            self.move = 'o'
            print('o')
        print('Coords: ', end='')
        x, y = [int(e) for e in input().split()]

        while self.place(x - 1, y - 1) == 0:
            print('you cant do it try, some different coords')
            print('Coords: ', end='')
            x, y = [int(e) for e in input().split()]
        self.moveX = not self.moveX

    def place(self, x, y):

        if self.board[y][x] == '-':
            self.board[y][x] = self.move
            return 1
        return 0

    def checkWin(self):
        for i in range(len(self.board)):
            if list('xxx') == self.board[i]:
                return 'x'
            elif list('ooo') == self.board[i]:
                return 'o'
        for i in range(len(self.board) - 2):
            for j in range(len(self.board[i])):
                if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == 'x':
                    return 'x'
                elif self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == 'o':
                    return 'o'
        return '-'

    def showBoard(self):
        for i in self.board:
            print('|', '|'.join(i), end='|\n', sep='')

    def haveEmptyField(self):
        for i in self.board:
            for j in i:
                if '-' in j:
                    return True
        return False


bb = Board()
n = 0
stop = False

while bb.haveEmptyField():
    bb.setCoordsThroughInput()
    bb.showBoard()
    if bb.checkWin() == 'x':
        stop = True
        print('*' * 6)
        print("X WON!")
        print('*' * 6)
        break
    elif bb.checkWin() == 'o':
        stop = True
        print('*' * 6)
        print("O WON!")
        print('*' * 6)
        break

if not stop:
    print("TIE, the friend is winner")
