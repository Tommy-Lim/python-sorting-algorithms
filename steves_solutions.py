def steve_bubble_sort(a, verbose=False):
  # ensure the while loop runs at least once
  first = True
  # simply count the number of times the outer
  # while loop runs.
  cycles = 0

  while(first is True or performed_swap is True):
    first = False
    performed_swap = False

    i = 0
    while i < (len(a) - 1):
      if a[i] > a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]
        performed_swap = True
      i += 1
    cycles += 1
    if verbose:
      print(cycles, a)
  return a

# This bucket sort assumes there are no negative numbers in the array.
def steve_bucket_sort(a):
  if len(a) < 1:
    return a

  # search for the largest value
  # "max" is a reserved keyword in python.
  maxx = a[0]
  for item in a:
    maxx = max(maxx, item)

  # create a list of all zeroes the size of maxx
  tally = [0] * (maxx + 1)

  # Go through the original array and increment the tally for
  # each number. The tallies are kept at the array index of the
  # value itself. Zeros are counted at index 0, ones are counted at index 1.
  for i, item in enumerate(a):
    tally[item] += 1

  # create a new array that will be the final sorted array
  sorted_a = []

  # iterate through each of the tallies for each value.
  for i, count in enumerate(tally):
    if count > 0:
      # Append the number to the sorted array the number of times that
      # it was tallied.
      # (use an underscore to indicate we're not using the value of i
      # we're just doing something i times.)
      for _ in range(count):
        sorted_a.append(i)
  return sorted_a

def steve_insertion_sort(a):
  # go over each spot in the array from beginning to end
  for i in range(len(a)):
    index = i
    min_value = a[i]
    # search the remaining array for the smallest value
    for n in range(i + 1, len(a)):
      if a[n] < min_value:
        min_value = a[n]
        index = n
    # swap the minimum value with the value at the location we're searching from.
    a[i], a[index] = min_value, a[i]
  return a

def steve_merge_sort(a):
  # single or zero-element arrays are always sorted!
  if len(a) < 2:
    return a

  # split a into two halves
  # force integer division.
  left = a[:len(a) // 2]
  right = a[len(a) // 2:]

  # recursively merge_sort those two halves
  a1 = steve_merge_sort(left)
  a2 = steve_merge_sort(right)

  # merge the two halves together by traversing each array in
  # order simultaneously and always taking the smaller of the two.
  sorted_a = []
  i1 = 0
  i2 = 0
  for _ in range(len(a1) + len(a2)):
    if not i1 < len(a1):
      sorted_a.append(a2[i2])
      i2 += 1
    elif not i2 < len(a2):
      sorted_a.append(a1[i1])
      i1 += 1
    elif a1[i1] < a2[i2]:
      sorted_a.append(a1[i1])
      i1 += 1
    else:
      sorted_a.append(a2[i2])
      i2 += 1
  return sorted_a
