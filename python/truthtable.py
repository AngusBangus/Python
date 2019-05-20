from logic import TruthTable

x = raw_input("Enter proposition 1: ")
y = raw_input("Enter proposition 2: ")






myTable1 = TruthTable(['p','q'], [x])
myTable2 = TruthTable(['p', 'q'], [y])

if(myTable1.table == myTable2.table):
	print("The Propositions are equivalent")
else:
	print("The propositions are not equivalent")

