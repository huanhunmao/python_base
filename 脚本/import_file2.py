import import_test2

scores = [1,2,3,4,5]

mean = import_test2.mean(scores)
curved = import_test2.add_five(scores)

mean_c = import_test2.mean(curved)

print('Scores', scores) # Scores [1, 2, 3, 4, 5]
print('Origin Mean: ', mean, ' New Mean: ', mean_c) # Origin Mean:  3.0  New Mean:  8.0