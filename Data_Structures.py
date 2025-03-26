# collections
# lists, dictionary, set
score = [78, 43, 78, 64, 56, 34, 90, 67, 87, 23, 59, 18, 70, 89, 85, 47, 50]

print(score[0])
print(score[1])

#add another score
score.append(51)
print(score)

#remove
score.remove(43)
print(score)

print(len(score))
print(score.count(51))


score.sort() #ascending
print(score)


score.sort(reverse=True) #descending manner
print(score)


#slice a list

top_5 = score[-5:]
print(top_5)

#dictionary

person = {"name": "Halima", "age" :19,"weight": 58,"county":"Nairobi"}
print(person["name"])
print(person["age"])

#set
days ={"mon", "tues", "wed", "thu", "fri", "sat", "sun","mon"}
print(days)

for s  in score:
    if s < 50:
        pass
    print(s)

for d in days:
    print(d)