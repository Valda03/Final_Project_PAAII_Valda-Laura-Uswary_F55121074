import time

def bubble(arr):
    a = len(arr)
    mulai = time.time()

    for i in range(a - 1):
        tukar = False

        for j in range(0, a - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                tukar = True

        if i < 5 or i >= a - 6:
            print("Iterasi ke-", i + 1, ":", arr)

    akhir = time.time()

    print("\nArray setelah diurutkan:")
    print(arr)

    print("\nWaktu komputasi yang dibutuhkan :", akhir - mulai, "detik")

def insertion(arr):
    a = len(arr)
    mulai = time.time()

    for i in range(1, a):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        if i < 5 or i >= a - 5:
            print("Iterasi ke-", i, ":", arr)

    akhir = time.time()

    print("\nArray setelah diurutkan:")
    print(arr)

    print("\nWaktu komputasi yang dibutuhkan :", akhir - mulai, "detik")

def main():
    array = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

    print("Pilihan Algoritma Sorting")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    pilih = int(input("Masukkan Pilihan Anda : "))

    if pilih == 1:
        print("\nBubble Sort")
        print("Array sebelum diurutkan:")
        print(array)
        print("\n")
        bubble(array[:])
    elif pilih == 2:
        print("\nInsertion Sort")
        print("Array sebelum diurutkan:")
        print(array)
        print("\n")
        insertion(array[:])
    else:
        print("Pilihan tidak valid.")

if __name__ == '__main__':
    main()
