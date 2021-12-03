def stack_sort(input_list):
    tempList = []
    while input_list:
        tempValue = input_list.pop()
        while tempList and tempList[-1] > tempValue:
            input_list.append(tempList.pop())   
        tempList.append(tempValue)
    return tempList

trial1 = [1, 5, 9, 2, 4, 3]
print(stack_sort(trial1)) # expected output: [1, 2, 3, 4, 5, 9]

trial2 = [20, 77, 31, 5, 8, 103, 66, 81]
print(stack_sort(trial2))  # expected output: [5, 8, 20, 31, 66, 77, 81, 103]