from numpy import arange, insert, int64, ones

def _filterPrimes(prime_array) -> list:
    is_prime = ones(len(prime_array), dtype=bool)

    for i, number in enumerate(prime_array):
        if is_prime[i]:  # Check if the number is still a potential prime
            is_prime[i+number::number] = False  # Filter out multiples of the current prime

    # Applies bool mask to initial array
    prime_array = list(prime_array[is_prime])
    return prime_array


def findPrimesUpTo(upper_bound: int):
    # Since our prime array starts at 3, if we begin elimanating multiples and iterate by a step each time, we should always have a prime next
    prime_array = arange(3, upper_bound, 2, dtype = int64)       # 3, 5, 7, 9, 11...upper_bound 

    filtered_list: list = _filterPrimes(prime_array)

    # Inserts 2 at the begining, since we skipped that originally.
    filtered_list.insert(0, 2)
    return filtered_list


def findNthPrime(length: int, upper_bound_modifier: int = 100000):
    filtered_list: list = []
    upper_bound:    int = upper_bound_modifier

    while length > len(filtered_list):
        prime_array     = arange(3, upper_bound, 2, dtype = int64)
        filtered_list   = _filterPrimes(prime_array)

        upper_bound     += upper_bound_modifier
    
    # Inserts 2 at the begining, since we skipped that originally.
    filtered_list.insert(0, 2)
    filtered_list = filtered_list[:length]
    return filtered_list