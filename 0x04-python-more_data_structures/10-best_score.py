#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    print(a_dictionary.values())
    sorted(a_dictionary.values())
    return a_dictionary.keys()[0]


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
