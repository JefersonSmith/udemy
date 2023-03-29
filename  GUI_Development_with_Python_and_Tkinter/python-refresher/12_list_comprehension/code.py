numers = [1, 3, 5]
doubled = [x * 2 for x in numers]
# for x in numers:
#     doubled.append(num * 2)
print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]
# starts_s = []
# for friend in friends:
#     if friend.startswith("S"): #Se o nome começa com S, adiciona na lista
#         starts_s.append(friend)

print(starts_s)