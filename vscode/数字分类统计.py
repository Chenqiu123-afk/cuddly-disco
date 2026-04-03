# 1.准备数字列表
nums = [1,2,3,4,5,6,7,8,9,10]
# 2.循环每一个数字
for n in nums:
    if n % 2 == 0:
        print(f"{n}是偶数")
    if n >= 6:
        print(f"{n}是大偶数")
    else:
        print(f"{n}是小偶数")        