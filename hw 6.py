def bubble_sort(num):
  n = len(num)

  for i in range(n):
    for j in range(0, n - i - 1):
      if num[j] > num[j + 1]:
        num[j], num[j + 1] = num[j + 1], num[j]


if __name__ == "__main__":
  num = [6, 9, 5, 2, 8, 4, 3, 7, 1]
  bubble_sort(num)
  print("отсортированный список1", num)


def  binary_search(х, number):
  low, high = 0, len(num) - 1
  while low <= high:
    mid = (low + high) // 2
    if num[mid] == х:
      return mid
    elif num[mid] < х:
      low = mid + 1
    else:
      high = mid - 1

  if low <= high:
    return 'element searched'
  else:
    return 'element not searched '
# binary_search(3,[1, 2, 3, 4, 5, 6, 7, 8, 9])
print(binary_search(7,[1, 2, 3, 4, 5, 6, 7, 8, 9]))
