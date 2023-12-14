def find_absolute_max_recursive(arr, current_max=None, index=0):
    if index == len(arr):
        return current_max
    absolute_value = abs(arr[index])
    if current_max is None or absolute_value > current_max:
        current_max = absolute_value
    return find_absolute_max_recursive(arr, current_max, index + 1)

def find_absolute_min_recursive(arr, current_min=None, index=0):
    if index == len(arr):
        return current_min
    absolute_value = abs(arr[index])
    if current_min is None or absolute_value < current_min:
        current_min = absolute_value
    return find_absolute_min_recursive(arr, current_min, index + 1)

def find_absolute_max(arr):
    absolute_values = map(abs, arr)
    max_absolute_value = max(absolute_values)
    return max_absolute_value

def find_absolute_min(arr):
    absolute_values = map(abs, arr)
    min_absolute_value = min(absolute_values)
    return min_absolute_value

def count_absolute_extremes(arr, extreme_value):
    absolute_values = map(abs, arr)
    count = sum(1 for value in absolute_values if value == extreme_value)
    return count

def main():
    real_numbers = [-2.5, 3.7, -1.8, 5.2, -1.8, 2.5]

    absolute_min = find_absolute_min(real_numbers)
    absolute_max = find_absolute_max(real_numbers)

    count_absolute_min = count_absolute_extremes(real_numbers, absolute_min)
    count_absolute_max = count_absolute_extremes(real_numbers, absolute_max)

    print(f"Наименьшее абсолютное значение: {absolute_min}")
    print(f"Наибольшее абсолютное значение: {absolute_max}")

    if count_absolute_min > 1:
        print(f"Количество наименьших абсолютных значений: {count_absolute_min}")

    if count_absolute_max > 1:
        print(f"Количество наибольших абсолютных значений: {count_absolute_max}")

if __name__ == "__main__":
    main()
