set1={1,2,4,38,4}
set2={2,8,1,5}
set3={5,4,8,6}

# it is used to add an element
set1.add(9)
print(set1)

# it is used to remove an element
set2.remove(2)
print(set2)

# it is used to clear the set
set3.clear()
print(set3)

# it is used to pop an element
set1.pop()
print(set1)

# it is used to combine all element(union)
set4=set1.union(set2)
print(set4)

# it is used to seprate common element(intersaction)

st1={4,5,9}
st2={48,2,4}
print(st1.intersection(st2))
