def min_time_to_paint(K, T, L):
    def is_valid(mid):
        painters = 1
        total = 0
        painters_work = [[]]  

        for length in L:
            if total + length > mid:
                painters += 1
                if painters > K:
                    return False
                painters_work.append([])  
                total = length
            else:
                total += length
            
            painters_work[-1].append(length)  

        return painters_work

    left, right = max(L), sum(L)
    result = right

    while left <= right:
        mid = (left + right) // 2
        print(f"\nПеревіряємо mid = {mid}, left = {left}, right = {right}")

        painters_work = is_valid(mid)
        if painters_work:
            print(f"Розподіл при mid = {mid}: {painters_work}")
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result * T

K, T, *L = map(int, input("Введіть K, T, L: ").split())
print(f"\n Мінімальний час для малярів: {min_time_to_paint(K, T, L)}")
