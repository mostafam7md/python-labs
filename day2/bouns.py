import time

def test_list():
    my_list = list(range(1_000_000))
    start = time.perf_counter()
    print(999_999 in my_list)  
    end = time.perf_counter()
    print(f"List time: {end - start:.6f} seconds - O(N) cause of linear search")

def test_set():
    my_set = set(range(1_000_000))
    start = time.perf_counter()
    print(999_999 in my_set)  
    end = time.perf_counter()
    print(f"List time: {end - start:.6f} seconds - O(1) cause of using hashing in search")
    


test_list()
test_set()