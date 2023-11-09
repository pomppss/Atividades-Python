numbers = []

for i in range(5):
    number = int(input(f"digite {i + 1} numero"))
    numbers.append(number)
numbers.sort()

print("O maior numero é o: ", numbers[-1])