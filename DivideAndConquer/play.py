# def threesum(arr):
#     result = []
#     for i in arr:
#         for j in arr:
#             for k in arr:
#                 out = i + j + k
#                 if out == 3:
#
#                     result.append([k,j,i])
#     return result
# #arr = [12, 3, 1, 2, -6, 5, -8, 6]
# arr = [6 , -3, 8, -7, 10, 2, 0]
# print(threesum(arr))
# def totalsum(arr):
#     if len(arr) == 0:
#         return 0
#     return arr[0] + totalsum(arr[1:])
# print(totalsum(arr))
# def threesum(array,targetsum):
#     array.sort()
#     triplets = []
#     for i in range(len(array) -2):
#         start = i + 1
#         stop = len(array) -1
#         while start < stop:
#             currentsum = array[i] + array[start] + array[stop]
#             if currentsum == targetsum:
#                 triplets.append([array[i], array[start], array[stop]])
#                 start += 1
#                 stop -= 1
#
#             elif currentsum < targetsum:
#                 start += 1
#             else:
#                 currentsum > targetsum
#                 stop -=1
#     return triplets
#
# #arr = [12, 3, 1, 2, -6, 5, -8, 6]
# #print(threesum(arr, 0))
#
# array1 = [-1, 5, 10, 20, 28, 3]
# array2 = [26, 134, 135, 15, 17]
# def smallestdifference(array1, array2):
#     check_num =


# a = [1,2,3,4,5]
# for i in range(len(a) // 2):
#     other = len(a) - i -1
#     print(other)

# Recur method

# def firstmethod():
#     secondmethod()
#     print("First Method Called")
# def secondmethod():
#     thirdmethod()
#     print("Second Method called")
# def thirdmethod():
#     fourthmethod()
#     print("Third Method Called")
# def fourthmethod():
#     print("Fourth Method called")
#
# firstmethod()

# def findmin(s, row, col):
#     if row == -1 or col == -1:
#         return float("inf")
#     elif row == 0 and col == 0:
#         return s[0][0]
#     else:
#         op1 = findmin(s, row -1, col)
#         op2 = findmin(s, row, col -1)
#         #print(  s[row][col],op1, op2)
#         return s[row][col] , op1, op2
s_arr = [
    [4,7,8,6,4],
    [6,7,3,9,2],
    [3,8,1,2,4],
    [7,1,7,3,7],
    [2,9,8,9,3]
]
print(s_arr[4][3])


