numbers = []

for i in range(5):
    number = int(input(f"digite {i + 1} numero: "))
    numbers.append(number)

sum_numbers = sum(numbers)
average = sum_numbers / len(numbers)

print("a soma dos numeros é:", sum_numbers)
print("a media dos numeros é:", average)