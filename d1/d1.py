# Initialize two empty lists to store the numbers
list1 = []
list2 = []

# Open the file and read one line at a time
with open('input.txt', 'r') as file:
    for line in file:
        # Split the line into two numbers
        num1, num2 = map(int, line.split())
        # Append the numbers to their respective lists
        list1.append(num1)
        list2.append(num2)

# Now you can use list1 and list2 for further processing


list1.sort()
list2.sort()

#sum the difference between each element in the two lists
sum = 0
for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])

#print(sum)

#calculate the similarity score between the 2 lists
#Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
total = 0
for i in list1:
    total += i * list2.count(i)

print(total)