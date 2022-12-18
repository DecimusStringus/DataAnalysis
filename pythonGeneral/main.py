data = ["a", "b", "a", "c", "a", "b"]
my_dict = {item: data.count(item) for item in data}
result1 = max(my_dict, key=my_dict.get) # another way to do it
result2 = max(my_dict, key=lambda var: my_dict[var])
# result3 = sorted(data, key=)
result4 = my_dict["a"]
print(result2)
