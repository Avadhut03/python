d1 = {"Simple":"easy", "hard":"difficult"}
d1["Avadhut"] = "Kulkarni"
del d1["Avadhut"]
d2=d1.copy()
d2["Avadhut"] = "Kulkarni"
#print(d1)
d2.update({"Shriniwas":"Kulkarni"})
print(d2.items())
