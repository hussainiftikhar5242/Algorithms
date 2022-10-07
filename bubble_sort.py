def bubbleSort(list):
    for num in range(len(list)):
        for i in range(num):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

list = [14,46,43,27,57,41,45,21,70]
bubbleSort(list)
print(list)
