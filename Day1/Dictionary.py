# student = {
#  "name": "Su Su",
#  "age": 20,
#  "score": 88,
#  "passed": True
# }

# print (student["name"])
# print (student["age"])
# print (student["passed"])
# print (student["score"])

students = [
 {"name": "Aung Aung", "score": 85},
 {"name": "Su Su", "score": 92},
 {"name": "Mg Mg", "score": 35}
]

for i in students:
    print (f"Name : {i["name"]},  Score : {i["score"]}")