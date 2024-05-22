cities = ['new york', 'chicago', 'los angels']

for city in cities:
    print(city.title())
    # New
    # York
    # Chicago
    # Los Angels

# append 方法 放入新的 中
newCities = []
for city in cities:
    newCities.append(city.title())

print(newCities) # ['New York', 'Chicago', 'Los Angels']

# range(start, stop, step)
print(list(range(4))) # stop [0, 1, 2, 3]
print(list(range(2,6)))  # start-stop [2, 3, 4, 5]
print(list(range(1, 10, 2))) # start-stop-step [1, 3, 5, 7, 9]

cities2 = ['beijing', 'shanghai', 'guangzhou']
# range(4) 结果是 [0,1,2,3]
for index in range(len(cities2)):
    cities2[index] = cities2[index].title()

print(cities2) # ['Beijing', 'Shanghai', 'Guangzhou']