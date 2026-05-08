from src.insertion_sort import insertion_sort
from src.merge_sort import merge

def hybrid_sort(arr, k=25, left=0, right=None):
    if right is None:
        right = len(arr) - 1
        
    # Se o pedaço for menor ou igual a K, usa Insertion Sort
    if (right - left + 1) <= k:
        insertion_sort(arr, left, right)
    else:
        # Senão, continua dividindo com Merge Sort
        if left < right:
            mid = left + (right - left) // 2
            hybrid_sort(arr, k, left, mid)
            hybrid_sort(arr, k, mid + 1, right)
            merge(arr, left, mid, right)