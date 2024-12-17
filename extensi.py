import random
import time
import matplotlib.pyplot as plt

def generate_array(n, max_value, seed):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]


def is_unique(arr):
    return len(arr) == len(set(arr))


def measure_time(func, arr):
    start_time = time.perf_counter()
    result = func(arr)
    end_time = time.perf_counter()
    return result, end_time - start_time


arr_sizes = [100, 150, 200, 250, 300, 350, 400, 500]
max_value = 208
seed = 42


results = []


for n in arr_sizes:
    arr = generate_array(n, max_value, seed)
    unique, time_taken = measure_time(is_unique, arr)
    results.append((n, unique, time_taken))
    print(f"Ukuran array: {n}, Keterangan: {'Unik' if unique else 'Tidak unik'}, Waktu: {time_taken:.6f} detik")

case_results = []
for n in arr_sizes:
    arr = generate_array(n, max_value, seed)
   
    _, worst_case_time = measure_time(is_unique, arr)
    
   
    avg_time = 0
    for _ in range(10):
        _, time_taken = measure_time(is_unique, arr)
        avg_time += time_taken
    avg_time /= 10

  
    case_results.append((n, avg_time, worst_case_time))
    print(f"Ukuran array: {n}, Waktu Kasus Rata-rata: {avg_time:.6f} detik, Waktu Kasus Terburuk: {worst_case_time:.6f} detik")



sizes = [n for n, _, _ in case_results]
avg_times = [avg_time for _, avg_time, _ in case_results]
worst_times = [worst_time for _, _, worst_time in case_results]

for n, avg_time, worst_case_time in case_results:
    plt.figure(figsize=(6, 4))
    
   
    x_values = ["Average Case", "Worst Case"]
    avg_y = [avg_time, avg_time]  
    worst_y = [worst_case_time, worst_case_time]  

   
    plt.plot(x_values, avg_y, marker='o', linestyle='-', color='blue', label="Average Case")
    plt.plot(x_values, worst_y, marker='x', linestyle='--', color='orange', label="Worst Case")
    
    plt.title(f"Average Case dan Worst Case untuk n = {n}")
    plt.ylabel("Waktu (detik)")
    plt.xlabel("Tipe Kasus")
    
    

    
   
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
