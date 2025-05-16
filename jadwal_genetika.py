import random

# Data simulasi
teachers = ['Guru A', 'Guru B', 'Guru C']
subjects = ['Matematika', 'Fisika', 'Kimia']
classes = ['Kelas 1', 'Kelas 2', 'Kelas 3']
timeslots = ['Senin P1', 'Senin P2', 'Selasa P1', 'Selasa P2']

# Individu: [guru, mata pelajaran, kelas, waktu]
def create_individual():
    return [
        random.choice(teachers),
        random.choice(subjects),
        random.choice(classes),
        random.choice(timeslots)
    ]

# Fungsi fitness: menghitung konflik
def fitness(individual, schedule):
    conflicts = 0
    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):
            if individual[2] == schedule[i][2] and individual[3] == schedule[i][3]:
                conflicts += 1
    return conflicts

# Seleksi: 2 individu terbaik
def selection(population, schedule):
    return sorted(population, key=lambda ind: fitness(ind, schedule))[:2]

# Crossover: pertukaran gen
def crossover(p1, p2):
    point = random.randint(1, 3)
    return (
        p1[:point] + p2[point:],
        p2[:point] + p1[point:]
    )

# Mutasi: perubahan acak
def mutate(individual):
    index = random.randint(0, 3)
    if index == 0:
        individual[index] = random.choice(teachers)
    elif index == 1:
        individual[index] = random.choice(subjects)
    elif index == 2:
        individual[index] = random.choice(classes)
    else:
        individual[index] = random.choice(timeslots)
    return individual

# Main GA
def genetic_algorithm():
    population = [create_individual() for _ in range(10)]
    schedule = []

    for gen in range(50):
        new_population = []
        for _ in range(5):
            p1, p2 = selection(population, schedule)
            c1, c2 = crossover(p1, p2)
            new_population.extend([mutate(c1), mutate(c2)])
        population = new_population
        best = min(population, key=lambda ind: fitness(ind, schedule))
        schedule.append(best)
        print(f"Generasi {gen+1}: {best} | Fitness: {fitness(best, schedule)}")

    print("\nJadwal Akhir:")
    for ind in schedule:
        print(f"{ind[2]} - {ind[1]} oleh {ind[0]} pada {ind[3]}")

# Jalankan
genetic_algorithm()
