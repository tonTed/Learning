def merge(A, p, q, r):
    """
    Fusion
    :param A (list)
    :param p (int)
    :param q (int)
    :param r (int)

    :return sortes list
    """
    n1 = q - p + 1
    n2 = r - q

    P = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        P[i] = A[p + i]
        
    for j in range(0, n2):
        R[j] = A[q + 1 + j]

    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if P[i] <= R[j]:
            A[k] = P[i]
            i += 1

        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = P[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

    
def merge_sort(A, p, r):
    """
    Recursive Function, work with fusion()
    :param A (list)
    :param p (int)
    :param r (int)

    :return sortted list
    """

    if p < r:
        q = (p+(r-1))//2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def fibonacci(A):
    """
    Fibonacci suite
    """
    if A > 1:
        return fibonacci(A -1) + fibonacci(A - 2)
    return 1