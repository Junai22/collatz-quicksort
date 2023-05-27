import random

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def generate_random_collatz_sequences(num_sequences, sequence_length):
    sequences = []
    for _ in range(num_sequences):
        n = random.randint(1, 100)  # Rango de números aleatorios
        sequence = collatz_sequence(n)
        if len(sequence) >= sequence_length:
            sequences.append(sequence[:sequence_length])
    return sequences

# Ejemplo de uso
num_sequences = 1  # Número de secuencias a generar
sequence_length = 10  # Longitud de cada secuencia

sequences = generate_random_collatz_sequences(num_sequences, sequence_length)
for sequence in sequences:
    print("Secuencia original:", sequence)
    sorted_sequence = quicksort(sequence)
    print("Secuencia ordenada:", sorted_sequence)
