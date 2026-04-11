def get_even_gt5(num_list):
    result = []
    for num in num_list:
        if num > 5 and num % 2 ==0:
            result.append(num)
    return  result
print(get_even_gt5([3,6,7,10,12,4]))