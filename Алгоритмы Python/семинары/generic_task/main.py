"""
Реализовать генетический алгоритм
"""

def next_generation(generation, offspring_size, survivivle_size, input_S):
    offsprings = []
    for memeber in generetion:
        offsprings += repoduce(member,offspring_size)
    next_generation = select(offsprings, input_S)

while True:
    generation = 
    generation_index += 0 