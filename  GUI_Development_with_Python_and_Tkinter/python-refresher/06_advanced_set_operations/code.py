friends = {"Bob", "Rolf" ,"Anne" }
abroad = {"Bob", "Anne"}
art = {"Bob", "Jen", "Rofl", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

local_friends = friends.difference(abroad)
friends1 = friends.union(abroad)
both = art.intersection(science)

print(local_friends)
print(friends1)
print(both)