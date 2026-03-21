Students = [[],
            []]
ttl = 0
with open("Results.txt", "r") as result:
    for line in result:
        a = line.split(",")
        Students[0].append(a[0])
        Students[1].append(int(a[1]))
        ttl += int(a[1])

#Total

print(Students)
print(f"average: {ttl/len(Students[0])}")

max = 0
name = ""
for i in range(len(Students[0])):
    if Students[1][i] > max:
        max = Students[1][i]
        name = Students[0][i]
print("Highest: " + name + " with " + str(max))

ctr = 0
for  i in range(len(Students[0])):
    if Students[1][i] > 80:
        print(Students[0][i] + " has more than 80 marks")
        ctr += 1

print("Number of students with more than 80 marks: " + str(ctr))
