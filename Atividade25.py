def is_population_higher_zero(population):
    return population > 0
def is_growth_rate_higher_zero(growth_rate):
    return growth_rate > 0
while True:
    population_a = 0
    while not is_population_higher_zero(population_a):
        population_a = int(input("Digite a população do país A: "))
        if not is_population_higher_zero(population_a):
            print("A população precisa ser maior do que zero!")

    population_b = 0
    while not is_population_higher_zero(population_b):
        population_b = int(input("Digite a população do país B: "))
        if not is_population_higher_zero(population_b):
            print("A população precisa ser maior do que zero!")
    growth_rate_a = 0.0
    while not is_growth_rate_higher_zero(growth_rate_a):
        growth_rate_a = float(input("Digite a taxa de crescimento do paísA (em decimal): "))
        if not is_growth_rate_higher_zero(growth_rate_a):
            print("A taxa de crescimento da população precisa ser maiordo que zero!")

    growth_rate_b = 0.0
    while not is_growth_rate_higher_zero(growth_rate_b):
        growth_rate_b = float(input("Digite a taxa de crescimento do paísB (em decimal): "))
        if not is_growth_rate_higher_zero(growth_rate_b):
            print("A taxa de crescimento da população precisa ser maiordo que zero!")
    years = 0
    if population_a > population_b:
        print("A população do país A já é maior do que a do país B!")
    elif growth_rate_a < growth_rate_b:
        print("A taxa de crescimento do país A deve ser maior do que ataxa de crescimento do país B!")
    else:
        while population_a < population_b:
            population_a += int(population_a * growth_rate_a)
            population_b += int(population_b * growth_rate_b)
            years += 1
            print(f"Após {years} anos, a população do país A ultrapassará apopulação do país B.\n")
            option = input("Deseja calcular novamente? (S/N): ").strip().lower()
            if option != 'n':
                break