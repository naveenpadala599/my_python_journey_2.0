class Runningsum:
    def __init__(self):
        self.total=0
    def update(self,value):
        self.total+=value
    def result(self):
        return self.total
rs=Runningsum()
rs.update(10)
rs.update(5)
print(rs.result())
