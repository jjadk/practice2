# for i in range(5):
#     print (i)
    
# score = [30, 45, 60, 37, 89]
# for i in score:
#     print ("Score : ", i)

# count = 1
# while count <= 5:
#     print (count)
#     count += 1

scores = [45, 70, 85, 30, 90, 55]

total = 0
fail_count = 0
pass_count = 0

for i in scores:
    
    total += i
    
for i in scores:
    if i < 40:
        fail_count +=1
    else:
        pass_count += 1
    
average = total / len(scores)
print ("Total : ", total)
print ("Average : ", average)
print ("Failling Count : ", fail_count)
print ("Passing Count : ", pass_count)
