# You are not allowed to import any modules whatsoever
# Assume a set is represented as a Python list
# Do not modify these
A = [1, 2, 5, 8, 12, 5]
B = [3, 5, 7, 8, 11, 3]
#1 simplify function
def simplify(A):
    result = []
    for i in A:
        if i not in result:
            result.append(i)
    return sorted(result)

print'A = ', simplify(A)

print'B = ', simplify(B)



print
#2 union function
def union(A, B):
    result = []
    for i in A+B:
        if i not in result:
            result.append(i)
    return result
      
print "A union B = ", union(A, B)
print


print

#3 intersection function
def intersection(A, B):
    result = []
    SB = simplify(B)
    for i in simplify(A):
        if i in SB:
            result.append(i)
    return result

print 'A intersection B = ', intersection(A, B)

print

#4 subset function
def subset(A, B):
    result = True
    for i in A:
        if not i in B:
            result = False
    return result

print 'A subset of B: ', subset(A, B)
print '[5, 7, 8] subset of B:', subset([5,7,8], B)

print

#5 equal function
def equal(A, B):
    return subset(A, B) and subset(B, A)

print 'A == B: ', equal(A, B)
print "[1, 2, 3, 4] == [1, 1, 2, 2, 4, 2, 3, 3]:", equal([1, 2, 3, 4],[1, 1, 2, 2, 4, 2, 3, 3])

print
#6 cartesian function
def cartesian_product(A, B):
    result = []
    SB = simplify(B)
    for i in simplify(A):
        for j in SB:
            result.append((i,j))
    return result

print "[1] x B =", cartesian_product([1], B)
print "[1, 2] x B =", cartesian_product([1, 2], B)
print "[A] x B =", cartesian_product(A, B)
print

#7power set
def power_set(A):
    if len(A) == 0:
        return [[]]
    else:
        head = A[0:-1]
        print "Head = ", A[0:-1]
        last = A[-1]
        print "Last = ", A[-1]
        temp = power_set(head)
        res = temp[:]
        print "temp = ", temp[:]

        for i in temp:
            print "i = ", i
            res.append(i+[last])
        return res

print "P([1, 2, 3]) =", power_set([1, 2, 3])
print "P([]) =", power_set([])
