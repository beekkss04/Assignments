import random

def has_same_birthday(n_people=23):
    birthdays = []
    for _ in range(n_people):
        
        day = random.randrange(1, 28)
        if day in birthdays:
            return True
        birthdays.append(day)
    return False

def simulate(trials=5000):
    count = 0
    for _ in range(trials):
        if has_same_birthday():
            count += 1
    probability = count / trials
    return probability

trials = 10000
prob = simulate(trials)
print(f"Probability that at least 2 people share birthday in a group of 23 = {prob:.4f}")