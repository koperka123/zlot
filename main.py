tab = ["Z", "K", "S", "E", "J", "U", "J", "O", "P", "N"]
array = []
for i in range(0, 10):
    array.append(ord(tab[i]))

# Zamieniamy tablice stringów (liter) na ordy dzięki czemu otrzymujemy ich
# wartosci liczbowe ktore sa latwiejsze do posortowania


# Funkcja partition dzięki pivotowi dzieli całą tablice na dwie mniejsze, gdzie
# w lewej znajdują się elementy mniejsze od pivota a po prawo większe od pivota

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


quick_sort(array, 0, len(array) - 1)

#Quicksort sortuje obie juz podzielone tablice i laczy je w calosc


def check_same_number():
    for x in range (0, len(array) - 1 ):
        if array[x] == array[x+1]:
            a = chr(array[x])
            return a

#Checksamenumber juz w posortowanej tablicy szuka dwoch takich samych wyrazow

print(check_same_number())