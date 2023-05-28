def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j]= arr[j],arr[i]
    return arr

input_str = input("enter the list of numbers:")
input_list = [int(num) for num in input_str.split(',')]

sorted_list = selectionSort(input_list)
unique_list= []
for num in sorted_list:
    if num not in unique_list:
        unique_list.append(num)
print("sorted list:",sorted_list)
print("unique sorted list:",unique_list)