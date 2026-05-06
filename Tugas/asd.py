def bubble_sort(arr):
  n = len(arr)

  for i in range(n):
    for j in range(0, n-i-1):

      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

  arr = [75, 36, 26, 15, 12, 89, 95]

  print("Sebelum diurutkan: ")
  print(arr)

  bubble_sort(arr)

  print("Setelah diurutkan: ")
  print(arr)