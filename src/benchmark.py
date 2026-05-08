import numpy as np
import time
import matplotlib.pyplot as plt
from src.insertion_sort import insertion_sort
from src.merge_sort import merge_sort
from src.hybrid_sort import hybrid_sort

def find_optimal_k():
    print("Step 1: Finding optimal K (Threshold)...")
    sizes = list(range(2, 101))
    time_ins, time_mer = [], []
    num_runs = 20

    for size in sizes:
        t_i, t_m = [], []
        for _ in range(num_runs):
            arr = np.random.randint(0, 1000, size)
            
            arr_i = arr.copy()
            start = time.perf_counter_ns()
            insertion_sort(arr_i)
            t_i.append(time.perf_counter_ns() - start)
            
            arr_m = arr.copy()
            start = time.perf_counter_ns()
            merge_sort(arr_m)
            t_m.append(time.perf_counter_ns() - start)
            
        time_ins.append(np.mean(t_i))
        time_mer.append(np.mean(t_m))

    optimal_k = 25 # Fallback
    for i in range(len(sizes)):
        if time_ins[i] > time_mer[i]:
            optimal_k = sizes[i]
            break
            
    # Graph 1: Threshold
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, time_ins, label='Insertion Sort')
    plt.plot(sizes, time_mer, label='Merge Sort')
    if optimal_k != -1:
        plt.axvline(x=optimal_k, color='red', linestyle='--', label=f'Threshold (K): N = {optimal_k}')
    plt.title('Execution Time Comparison for Small Inputs')
    plt.xlabel('Input Size (N)')
    plt.ylabel('Average Execution Time (ns)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print(f"-> Optimal K found: {optimal_k}\n")
    return optimal_k

def run_main_benchmark(k):
    sizes = [100, 1000, 5000, 10000]
    num_runs = 3
    
    scenarios = ['Random', 'Ascending', 'Descending']
    results = {
        'Insertion': {s: [] for s in scenarios},
        'Merge': {s: [] for s in scenarios},
        'Hybrid': {s: [] for s in scenarios}
    }
    
    print(f"Step 2: Running main benchmark with K = {k}...")
    for size in sizes:
        print(f"  Testing size {size}...")
        temps = {alg: {s: [] for s in scenarios} for alg in results}
        
        for _ in range(num_runs):
            base_rand = np.random.randint(0, size * 10, size)
            base_asc = np.sort(base_rand)
            base_desc = base_asc[::-1].copy()
            
            arrays = {
                'Random': base_rand,
                'Ascending': base_asc,
                'Descending': base_desc
            }
            
            for scenario, base_arr in arrays.items():
                # Insertion
                arr_copy = base_arr.copy()
                start = time.perf_counter_ns()
                insertion_sort(arr_copy)
                temps['Insertion'][scenario].append(time.perf_counter_ns() - start)
                
                # Merge
                arr_copy = base_arr.copy()
                start = time.perf_counter_ns()
                merge_sort(arr_copy)
                temps['Merge'][scenario].append(time.perf_counter_ns() - start)
                
                # Hybrid
                arr_copy = base_arr.copy()
                start = time.perf_counter_ns()
                hybrid_sort(arr_copy, k)
                temps['Hybrid'][scenario].append(time.perf_counter_ns() - start)
                
        for alg in results:
            for scenario in scenarios:
                results[alg][scenario].append(np.mean(temps[alg][scenario]))
                
    # Graphs 2, 3 and 4
    for scenario in scenarios:
        plt.figure(figsize=(10, 6))
        plt.plot(sizes, results['Insertion'][scenario], label='Insertion Sort', marker='o')
        plt.plot(sizes, results['Merge'][scenario], label='Merge Sort', marker='x')
        plt.plot(sizes, results['Hybrid'][scenario], label=f'Hybrid Sort (K={k})', marker='s')
        plt.title(f'Performance Comparison: {scenario} Array')
        plt.xlabel('Input Size (N)')
        plt.ylabel('Average Execution Time (ns)')
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    optimal_k = find_optimal_k()
    run_main_benchmark(optimal_k)