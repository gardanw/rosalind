def mer(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
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
    return out


def ms(arr):
    if len(arr) < 2:
        return arr
    arr1 = arr[:len(arr)//2]
    arr1 = ms(arr1)
    arr2 = arr[len(arr)//2:]
    arr2 = ms(arr2)
    return mer(arr1, arr2)


with open("rosalind_ms.txt", 'r') as file:
    len_arr = int(file.readline())
    arr = list(map(int, file.readline().split()))


print(" ".join(map(str, ms(arr))))
