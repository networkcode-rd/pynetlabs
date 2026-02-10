emp = {"emp1":{"name":"Ratnavo"},
       "emp2": {"name": "Chirag"},
       "emp3": {"name": "Putul"}}

print(emp)
print(emp["emp3"]["name"])

emp.update({"emp4": {"name": "Nitish", "role":"Sales_head","domain":"Sales"}})
print(emp)

emp["emp4"]["domain"]="PaloAlto"
print(emp)

emp["emp1"]["location"] = "Delhi"
print(emp)

emp["emp4"].pop("role")
print(emp)

# emp["emp1"]["courses"] = ["CCNA","CCNP","CCIE"] == One way
emp["emp1"].update({"courses": ["CCNA","CCNP","CCIE"]})
print(emp)
print(emp["emp1"]["courses"][2])