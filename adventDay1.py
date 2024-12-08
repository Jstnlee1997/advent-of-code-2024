import collections

# parse inputs
list1, list2 = [], []
f = open("adventday1", "r")
for row in f:
    nums = row.split()
    list1.append(int(nums[0]))
    list2.append(int(nums[1]))
f.close()

list1.sort()
list2.sort()

# Part 1
# diff = 0
# for i in range(len(list1)):
#     diff += abs(list1[i] - list2[i])
# print(diff)

# Part 2
ret = 0
similarityScores = collections.defaultdict(int)
for num1 in list1:
    if num1 not in similarityScores:
        for num2 in list2:
            if num1 == num2:
                similarityScores[num1] += num1
    ret += similarityScores[num1]

print(ret)
