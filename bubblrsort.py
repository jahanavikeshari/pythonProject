class sorting:
    def bubble_sort(self, arr):
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        print(arr)


arr = [8, 5, 6, 45, 34, 98, 23]
l = []
size = int(input("Enter the size of the array"))
for i in range(size):
    z = int(input("Please enter the next value"))
    l.append(z)
print(l)
ob = sorting()
ob.bubble_sort(l)
