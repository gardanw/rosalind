with open("rosalind_mer.txt", 'r') as file:
    len1 = int(file.readline())
    arr1 = list(map(int, file.readline().split()))

    len2 = int(file.readline())
    arr2 = list(map(int, file.readline().split()))

out = []
index1 = 0
index2 = 0

while index1 != len1 and index2 != len2:
    if arr1[index1] < arr2[index2]:
        out.append(arr1[index1])
        index1 += 1
    elif arr1[index1] > arr2[index2]:
        out.append(arr2[index2])
        index2 += 1
    elif arr1[index1] == arr2[index2]:
        out.append(arr1[index1])
        out.append(arr2[index2])
        index1 += 1
        index2 += 1

if index1 < len1:
    out += arr1[index1:]
elif index2 < len2:
    out += arr2[index2:]

print(" ".join(map(str,out)))
