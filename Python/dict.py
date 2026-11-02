'''laptop1={"name":"Asus Tuff",
         "Ram":"12Gb",
         "Storage":"1Tb"}
print(laptop1["name"])
print(laptop1.get("Ram"))'''
stu1={"name":"Airaf",
      "ERP":159,
      "Branch":"CSE"}
for i in stu1.keys():
    print(i)
for i in stu1.items():
    print(i)
for i in stu1.values():
    print(i)