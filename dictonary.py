# key - value 

dictinary={"reg":"repression",
            "log": "logistic regression ",
             "cart" : "classification and reg" }

a_dictinary={"tom" : [101, "andrew"],
             "mary": [230,"holland"],
             "jon":  [460, "snow"]
             }

print(dictinary["reg"])

print(a_dictinary["mary"][1])

print("jon" in a_dictinary)


print(dictinary["reg"])

print(dictinary.get("reg"))

dictinary["reg"] = "rain" 
print(dictinary)

print(dictinary.keys())

print(dictinary.values())

print(dictinary.items())

dictinary.update({"reg":10})
dictinary.update({"re":100})

print(dictinary)
