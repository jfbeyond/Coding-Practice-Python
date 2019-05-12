


# sweep the matrix until reaching the coordinate


class trackCoins(object):

    def __init__(self,rows,cols):
        self.cache = [[0]*cols for _ in range(rows)]
        self.rows = rows
        self.cols = cols
        # print(self.cache, self.rows, self.cols)
        
    # def printca(self):
    #     print(self.cache)

    def track(self,loc):

        if loc[0] > self.rows or loc[1] > self.cols:
            
            print('Invalid point, max rows = ', self.rows, 'max cols = ', self.cols)
            return

        if self.cache[loc[0]][loc[1]] == 1:
            return True
        else:
            self.cache[loc[0]][loc[1]] = 1
        
        return False

test1 = trackCoins(5,5)
# test1.printca()
print(test1.track([1,2]))
print(test1.track([1,2]))
print(test1.track([7,2]))
