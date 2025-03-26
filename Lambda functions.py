from functools import reduce


def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(10, 20))

add_two =lambda a, b: a + b

print(add_two(10, 20))

scores = [{"eng": 56, "math": 60},
          {"eng": 23, "math": 97},
          {"eng": 45, "math": 63},
          {"eng": 98, "math": 70}]

sorted_by_maths = sorted(scores, key=lambda s: s["math"])
print(sorted_by_maths)

def get_eng_scores(scores):
    return scores["eng"]

sorted_by_eng = sorted(scores, key=get_eng_scores)

print(sorted_by_eng)

ages = [55,66,23,14,35,78,98,12,16,23,12,56,76,54,32,21,76,54,46,78,34]

total_ages = reduce(lambda x, y: x + y, ages,0)
print(total_ages)

new_ages = map(lambda x: x + 1, ages)
print(list(new_ages))
 # TODO lambda functions
above_60 = filter(lambda x: x > 60, ages)

print(list(above_60))



