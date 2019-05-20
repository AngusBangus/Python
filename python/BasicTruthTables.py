from logic import TruthTable

myTable = TruthTable(['p', 'q', 'r']['p -> q', 'q -> r', ' p -> r'])
myTable.display()
myTable.latex()