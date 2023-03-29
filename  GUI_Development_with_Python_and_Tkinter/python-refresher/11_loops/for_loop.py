friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend.")
# print(f"{friends[0]} is my friend.")
# print(f"{friends[1]} is my friend.")
# print(f"{friends[2]} is my friend.")
# print(f"{friends[3]} is my friend.")
for friend in range(4):
    print(f"{friend} is my friend.")

grades = [35, 67, 98, 100, 100]
total = sum(grades) #soma
amount = len(grades)

# total = 0
# for grade in grades:
#     total += grade

print(total / amount) #media

