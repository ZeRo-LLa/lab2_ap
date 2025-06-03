import unittest

def is_monotonic(arr):

    increasing = decreasing = True
    anomalies = []
    anomaly_start = None  

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:  
            decreasing = False
            if anomaly_start is not None:  
                anomalies.append((anomaly_start + 1, i)) 
                anomaly_start = None  
        elif arr[i] < arr[i - 1]:  
            increasing = False
            if anomaly_start is None:  
                anomaly_start = i - 1

    if anomaly_start is not None:  
        anomalies.append((anomaly_start + 1, len(arr)))  

    return increasing or decreasing, anomalies

user_input = input("Введіть масив чисел через пробіл: ")
arr = list(map(int, user_input.split()))

monotonic, anomalies = is_monotonic(arr)

if monotonic:
    print("True")
else:
    formatted_anomalies = ", ".join(f"{end} {start}" for start, end in anomalies)  
    print(f"Індекс аномалій: {formatted_anomalies} False")
