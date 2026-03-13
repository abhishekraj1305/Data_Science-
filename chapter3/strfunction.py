a = "ghelghoeibghqeloehvoewiytlwqwiuivqytpthbsdddfhhsdd"

# print(a[0])  # g
# print(a[1])  # h    

# print(a[2:40:2])  # e


# print(a[::3])  # ghohqlhvewqwiuivqytpthbsdddfhhsdd

print(len(a))  # 56
print(a.capitalize())  # Ghelghoeibghqeloehvoewiytlwqwiuivqytpthbsdddfhhsdd
print(a.upper())  # GHELGHOEIBGHQELOEHVOEWY
print(a.lower())  # ghelghoeibghqeloehvoewiytlwqwiuivqytpthbsdddfhhsdd
print(a.count("h"))  # 6
print(a.find("h"))  # 1
print(a.replace("h", "H"))  # gHelgHoeibgHq
print(a.split("h"))  # ['g', 'elg', 'oeibg', 'qeloe', 'voewiytlwqwiuivqytptbsdddf', 'sdd']
print(a.strip("g"))  # helghoeibghqeloehvoewiytlwqwiuivqytpthbsdddfhhsdd
print(a.startswith("g"))  # True
print(a.endswith("d"))  # True
print(a.isalpha())  # False
