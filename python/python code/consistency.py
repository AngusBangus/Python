from logic import TruthTable

List = []
end = False

while not end:
    propVar = raw_input("Enter a proposition:")
    List.append(propVar)
    more = raw_input("Would you like to enter more?(Y/N):")
    if more == 'N':
        end = True

propTable = TruthTable(List)

consistent = False
for i in range(len(propTable.table )):
    if propTable.table[i][1] == [1]*len(List):# double check it
        consistent = True
        break

if consistent:
    print('Your description is consistent')
else:
    print('Your description is not consistent')


