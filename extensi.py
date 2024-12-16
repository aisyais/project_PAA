import random
import time
import matplotlib.pyplot as plt

def generate_array(n, max_value, seed=42):
    random.seed(seed)
    return [random.randint(0, max_value) for _ in range(n)]

def is_unique(array):
    seen = set()
    for num in array:
        if num in seen:
            return False  # Not unique
        seen.add(num)
    return True  # Unique

def calculate_worst_case(n):
    return n  # Worst case assumes comparing all elements

def calculate_average_case(n):
    return n / 2  # Average case assumes checking roughly half the elements

# Parameters
n_values = [100, 150, 200, 250, 300, 350, 400, 500]
max_value = 208
seed = 42

# Data for plotting
worst_case_times = []
average_case_times = []

for n in n_values:
    array = generate_array(n, max_value, seed)
    
    # Timing worst case
    start_time = time.time()
    _ = is_unique(array)  # Simulate the uniqueness check
    end_time = time.time()
    worst_case_time = calculate_worst_case(n)
    worst_case_times.append(worst_case_time)
    
    # Calculate average case
    average_case_time = calculate_average_case(n)
    average_case_times.append(average_case_time)

# Plotting
for i, n in enumerate(n_values):
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, worst_case_times, label='Worst Case', marker='o')
    plt.plot(n_values, average_case_times, label='Average Case', marker='x')
    plt.title(f"Worst Case and Average Case Analysis for n={n}")
    plt.xlabel("Array Size (n)")
    plt.ylabel("Number of Operations")
    plt.legend()
    plt.grid(True)
    plt.show()
