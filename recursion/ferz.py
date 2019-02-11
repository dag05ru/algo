class Ferz:
    def __init__(self, n):
        self.n = n
        self.diag1 = [[0 for i in range(n)] for i in range(n)]
        self.diag2 = [[0 for i in range(n)] for i in range(n)]
        self.col =   [[0 for i in range(n)] for i in range(n)]
        self.board =  [[0 for i in range(n)] for i in range(n)]


    def insert(self, x, y, val):
        n = self.n
        for i in range(n):
            self.col[i][x] = val
        
        tx, ty = x, y
        while tx < n and ty >= 0:
            self.diag1[ty][tx] = val
            tx += 1
            ty -= 1
        
        tx, ty = x, y
        while tx >= 0 and ty < n:
            self.diag1[ty][tx] = val
            tx -= 1
            ty += 1

        tx, ty = x, y
        while tx >= 0 and ty >= 0:
            self.diag2[ty][tx] = val
            tx -= 1
            ty -= 1

        tx, ty = x, y
        while tx < n and ty < n:
            self.diag2[ty][tx] = val
            tx += 1
            ty += 1


    def print_arr(self, arr):
        for e in arr:
            print(e)


    def calc(self, y):
        if y == self.n: 
            self.count += 1
            self.print_arr(self.board)
            print()
            return
        for x in range(self.n):
            if not (self.col[y][x] or self.diag1[y][x] or self.diag2[y][x]):
                self.board[y][x] = 9
                self.insert(x,y,1)
                self.calc(y+1)
                self.board[y][x] = 0
                self.insert(x,y,0)
            


    def solution(self):
        self.count = 0
        self.calc(0)


f = Ferz(8)
f.solution()
print(f.count)



