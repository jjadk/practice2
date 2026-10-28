scores = [55, 80, 35, 90, 65]

scores.append(75)
print (scores)

scores[1] = 85
print (scores)

print ("Highest Score : ", max(scores))
print ("Lowest Score : ", min(scores))

average = sum(scores) / len(scores)
print (average)

print ("\nScores of 80 or above -")
for i in scores:
    if i >= 80:
        print (i)
