"""
https://en.wikipedia.org/wiki/Bubble_sort

Barack Obama at Google answers "what is the most efficient way to sort
a million 32-bit integers?"
https://www.youtube.com/watch?v=k4RRi_ntQc8

Bubble sort is not the most efficient sorting algorithm in the world.
In fact, it's one of the worst. Still, it works. Let's see how it works.

Bubble Sort iterates through an array and swaps any two values that are
next to each other that are out of order. It does this over and over
until it passes through the array without swapping any values.

start i at 1 and look backwards to prevent running off end of array.
original = [4, 3, 2, 6, 5, 1]
swap 4,3   [4, 3, 2, 6, 5, 1]
            \  /
swap 4,2   [3, 4, 2, 6, 5, 1]
               \  /
keep 4,6   [3, 2, 4, 6, 5, 1]
                  |  |
swap 6,5   [3, 2, 4, 6, 5, 1]
                     \  /
swap 6,1   [3, 2, 4, 5, 6, 1]
                        \  /
4 swaps    [3, 2, 4, 5, 1, 6]
repeat     [3, 2, 4, 5, 1, 6]
swap 3,2   [3, 2, 4, 5, 1, 6]
            \  /
keep 3,4   [2, 3, 4, 5, 1, 6]
               |  |
keep 4,5   [2, 3, 4, 5, 1, 6]
                  |  |
swap 5,1   [2, 3, 4, 5, 1, 6]
                     \  /
keep 5,6   [2, 3, 4, 1, 5, 6]
                        |  |
2 swaps    [2, 3, 4, 1, 5, 6]
repeat     [2, 3, 4, 1, 5, 6]
keep 2,3   [2, 3, 4, 1, 5, 6]
            |  |
keep 3,4   [2, 3, 4, 1, 5, 6]
               |  |
swap 4,1   [2, 3, 4, 1, 5, 6]
                  \  /
keep 4,5   [2, 3, 1, 4, 5, 6]
                     |  |
keep 4,5   [2, 3, 1, 4, 5, 6]
                        |  |
keep 5,6   [2, 3, 1, 4, 5, 6]
keep 5,6   [2, 3, 1, 4, 5, 6]
keep 5,6   [2, 3, 1, 4, 5, 6]
1 swap
repeat


"""
def bubble_sort(a, verbose=False):
    sorting = True
    while sorting == True:
        swaps = 0
        for i in range(1,len(a)):
            if a[i] < a[i-1]:
                swaps =+ 1
                a[i], a[i-1] = a[i-1], a[i]
            if i == len(a)-1 and swaps == 0:
                sorting = False
    # print(a)
    return a

"""
https://en.wikipedia.org/wiki/Bucket_sort

The general idea of bucket sort is to go through an array and tally up
how many times each value occurs, then to generate a new array made up
of the values in order with each value appearing the same number of times
it appeared in the original array.

To keep things easy, we'll allow this implementation of bucket sort to assume
there are no negative numbers in the array.

Psuedo-code algorithm:
- Assume the minimum value in the array is zero.
- Make one pass through the array to find it's max value.
- Create an array of size zero - MAX
- Make a second pass through the array to tally how often each
  number occurs. Save each tally in the array from 0-MAX that
  was created. The value at each index of the array represents
  how many times the index occurred as a value in the original
  array.
- Finally, overwrite the original array by iterating through the
  tally array by it's index and adding each index as a value according
  to how many times it was tallied.

original = [5, 1, 0, 5, 0, 1, 0, 0, 0, 3, 0, 5]
MAX = 5
        # index  0  1  2  3  4  5
initial tally = [0, 0, 0, 0, 0, 0]
  final tally = [6, 2, 0, 1, 0, 3]

There were 6 zeroes, 2 ones, zero twos, 1 three, zero fours and 3 fives.

Now, overwrite the original array by stepping through the final tally and
adding the index as a value as many times as it was tallied:

  [0, 0, 0, 0, 0, 0,  # add six zeroes
   1, 1               # add two ones
   3,                 # add one three
   5, 5, 5]           # add three fives.

And there you have it. You've generated a sorted array.
"""
def bucket_sort(a):
    maxx = a[0]
    for num in a:
        if num > maxx:
            maxx = num
    arr = [0] * (maxx + 1)
    for num in a:
        arr[num] += 1
    a = []
    for i in range(0,len(arr)):
        if arr[i] > 0:
            a += [i]*arr[i]
    # print(a)

    return a

# https://en.wikipedia.org/wiki/Insertion_sort
def insertion_sort(a):
    for i in range(len(a)):
        min_value = a[i]
        index = i
        for j in range(i+1, len(a)):
            if a[j] < min_value:
                index = j
                min_value = a[j]
        a[i], a[index] = min_value, a[i]

    # print(a)
    return a

"""
https://en.wikipedia.org/wiki/Merge_sort

What are the two easiest lists to sort? An empty list, and a single-item
list.

How hard is it to create one large sorted array by merging together two
smaller sorted arrays? Not hard.

Merge sort is a recursive search algorithm built on these two premises.
It takes one array and splits it in half over and over again until their
small and sorted, then it merges small sorted pieces together on their
way back up.

Notice that the algorithm continues to split arrays until they're down
to single-item arrays. The split step does not check to see if arrays
are sorted. It relies on the fact that zero or single-element arrays
are fundamentally sorted and only returns those.

Pseudo-code:
  function:
    - if the array contains zero or one elements return it.
    - split the array into left and right halves
    - recursively merge_sort the left half
    - recursively merge_sort the right half
    - now the halves are guaranteed to be sorted
    - run a merge algorithm to merge the two sorted arrays into one
    - return the now-sorted array.

Here's a diagram of what happens:

                     [9, 2, 7, 4, 6, 1, 3, 5, 8]
split               /                           \
              [9, 2, 7, 4]                [6, 1, 3, 5, 8]
split        /            \              /               \
          [9, 2]        [7, 4]        [6, 1]          [3, 5, 8]
split    /      \      /      \      /      \        /         \
       [9]      [2]  [7]      [4]   [6]     [1]    [3]       [5, 8]
         |      |      |      |      |      |        |       /    \   split
         |      |      |      |      |      |        |     [5]    [8]
         |      |      |      |      |      |        |       \    /   merge
         |      |      |      |      |      |        |       [5, 8]
merge    \      /      \      /      \      /        \         /
          [2, 9]        [4, 7]        [1, 6]          [3, 5, 8]
merge        \            /              \               /
              [2, 4, 7, 9]                [1, 3, 5, 6, 8]
merge               \                           /
                     [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
def merge_sort(a):
    if len(a) < 2:
        return a
    else:
        middle = len(a)//2
        left = a[:middle]
        right = a[middle:]
        result = merge(merge_sort(left), merge_sort(right))
        # print("result", result)
        return result


def merge(arr1, arr2):
    if arr1 is None:
      return arr2
    elif arr2 is None:
      return arr1

    i1 = 0
    i2 = 0
    result = []

    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] < arr2[i2]:
            result.append(arr1[i1])
            i1 +=1
        else:
            result.append(arr2[i2])
            i2 +=1
    result += arr1[i1:]
    result += arr2[i2:]
    return result
