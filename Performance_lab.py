
# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    # Your code here
`   most_common = numbers[0]
    max_count = 0

    for num in numbers:
        count = 0
        for other in numbers:
            if num == other:
                count += 1
        if count > max_count:
            max_count = count
            most_common = num

    return most_common

#print(most_frequent([1, 3, 2, 3, 4, 1, 3]))
# Output: 3

"""
Time and Space Analysis for problem 1:
- Best-case:O(n^2)- If the first element is the most frequent, it still has to go through the whole list
- Worst-case:O(n^2)- If the last element is the most frequent, it still has to go through the whole list
- Average-case:O(n^2)- On average, it will have to go through the whole list for each number
- Space complexity:0(1) - Only a few variables are used regardless of input size
- Why this approach?- It is simple for coders, it is what I have learned in my other coding classes. It uses built in functions
- Could it be optimized?- Yes, after doing some research, I found that using a dictionary would be faster and more efficient
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    # Your code here
    sett = set()
    output = []
    for num in nums:
        if num not in sett:
            sett.add(num)
            output.append(num)
    return output
#print(remove_duplicates([4, 5, 4, 6, 5, 7]))  
# Output: [4, 5, 6, 7]


"""
Time and Space Analysis for problem 2:
- Best-case: 0(n) - If there are no duplicateds, it only has to go throught the list once
- Worst-case: 0(n) - If all the numbers are duplicated, it still has to go through the whole list once
- Average-case: 0(n) - On average, it will have to go through the whole list once
- Space complexity: 0(n) - The set and output list can grow with the input size, so it all depends on how many unique numbers there are
- Why this approach? Using sets allows fast checks for duplicates, and lists preserve order
- Could it be optimized? - I think this is the best approach. I used this same strategy in my timed problem last week.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    # Your code here
    sett = set()
    pairs = []

    for num in nums:
        match = target - num
        if match in sett:
            pairs.append((match, num))
        sett.add(num)

    return pairs
#print(find_pairs([1, 2, 3, 4], 5))
# Output: [(1, 4), (2, 3)]


"""
Time and Space Analysis for problem 3:
- Best-case: 0(n) - If the first two numbers sum to the target, it still has to go through the whole list once
- Worst-case: 0(n) - If the last two numbers sum to the target, it still has to go through the whole list once
- Average-case: 0(n) - On average, it will have to go through the whole list once
- Space complexity: The set and pairs list can grow with the input size, so it all depends on how big the list is and how many pairs there are
- Why this approach? It is efficient and simple, using a set allows for lookups no matter the list size
- Could it be optimized? - I cannot find a better approach than this one
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    # Your code here
    items = []
    for i in range(n):
        items.append(i)
    return items

#print(add_n_items(6))
#Output:[0, 1, 2, 3, 4,5]
#I could not figure out the doubling part but this is the fisrt part I think


"""
Time and Space Analysis for problem 4:
- When do resizes happen? - resizes happen when the list reaches its current capacity. Python then doubles it automatically
- What is the worst-case for a single append? - O(n) - When a resize happens, all elements need to be copied to the new list
- What is the amortized time per append overall? - O(1) - the average time per append remains constant unless the list becomones abnrmally large
- Space complexity: If the list reaches its limit python usually doubles its size for storage. That is what this problem is doing manually.
- Why does doubling reduce the cost overall? This is because it reduces how often it resizes and only resizes when the limit is reached
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    # Your code here
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result

#print(running_total([1, 2, 3, 4]))
# Output: [1, 3, 6, 10]

"""
Time and Space Analysis for problem 5:
- Best-case:0(n) - It has to go through the whole list once
- Worst-case: 0(n) - It has to go through the whole list once
- Average-case: 0(n) - On average, it will have to go through the whole list once
- Space complexity: A new list is created to store the running totals. This is optimal unless the list gets too large
- Why this approach? This approach is simple and uses built in functions. It also uses only one loop
- Could it be optimized? Yes the only think that could be changed to save storage is by appending the same list so it doesnt have to store a new one

"""
