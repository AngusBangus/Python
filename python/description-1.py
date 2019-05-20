from logic import TruthTable
meaningList = []
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
    print("Your program uses propositional variable " + str(propTable.vars))
    for i in range(len(propTable.vars)):
        meaning = raw_input("Enter the meaning of " + propTable.vars[i] + ": ")
        meaningList.append(meaning)


    print('Your description is consistent when')

    for i in meaningList:
            if (propTable.table[0][0][0] != propTable.table[0][1][0]):
                print("It is not the case that " + i)
            else:
                print("It is the case that " + i)

else:
    print('Your description is not consistent')


