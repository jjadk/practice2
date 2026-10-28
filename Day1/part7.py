# def greet (name):
#     print (f"Hello {name}")
    
# greet("Nyi Nyi")

# def calculate (scores):
    
#     if len(scores) == 0:
#         return 0
    
#     return sum(scores) / len (scores)

# scores = [70, 80, 90]
# result = calculate(scores)

# print ("Total : ", sum(scores))
# print ("Average : ", result)

def calculate_total (scores):
    
    if len(scores) == 0:
        return 0
    
    total = 0
    for i in scores:
        total +=i
    return total

def calculate_average (scores):
    
    if len(scores) == 0:
        return 0
    
    return sum(scores) / len (scores)

def classify_grade(i):
    
        if i < 0 or i >100:
            return "Invalid"
        
        elif i >= 80:
            return "Excellent"
        
        elif i >= 60:
            return "Good"
        
        elif i >=  40:
            return "Pass"
        
        else:
            return "Fail"

def count_passed(scores):
    
    if len(scores) == 0:
        return 0
    
    count = 0
    for i in scores:
        if i > 40:
            count += 1
    return count
        
scores = [45, 70, 85, 30, 90, 55]

total = calculate_total(scores)
average = calculate_average(scores)
counting_pass = count_passed(scores)

print ("Total : ", total)
print ("Average : ", average)
print ("Grade : ", classify_grade(87))
print ("Pass Count : ", counting_pass)