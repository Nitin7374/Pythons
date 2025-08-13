dict ={ 
    "name":"nitin",
    "class": "BCA",
    "marks":{
        "physics":65,
        "chemistry":85,
          }
}

# returing all keys using method
print(len(list(dict.keys())))

print(tuple(dict.keys()))

# returing all values using method
print(dict.values())

# returing all (keys,value) pairs as tuple

pairs =list((dict.items()))
print(pairs[1])

# returing the key according to values

print(dict.get("name1"))
print(dict.get("name"))

# inserts the specified items to the dictionary
dict.update({"city": "jaipur"})
print(dict)