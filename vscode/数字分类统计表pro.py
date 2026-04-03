while True:
    print("=====================")
    print("欢迎你的到来")
    print("=====================")

    print("1.奇数/偶数分类")
    print("2.小数/中数/大数分类")
    print("3.退出程序")

    choice = input("请选择功能1/2/3")
    if choice == "3":
        print("退出程序")
        break
    elif choice in("1","2"):
        while True:
            try:
                start = int(input("请输入开始数字:"))
                print(f"你输入的数字是：{start}")
                break
            except ValueError:
                print("输入错误,请输入有效数字")
        while True:
            try:
                end = int(input("请输入结束数字:"))
                print(f"你输入的数字是:{end}")
                break
            except ValueError:
                print("输入错误,请输入有效数字")

    nums = list(range(start,end+1))        
    
    count_odd = 0
    count_even = 0
    count_small = 0
    count_mid = 0
    count_large = 0

    if choice == "1":
        print("\n===偶数/奇数分类结果===")
        for n in nums:
            if n % 2 == 0:
                print(f"{n}是偶数")
                count_even = count_even + 1
            else:
                print(f"{n}是奇数")
                count_odd = count_odd + 1
        print(f"偶数一共有：{count_even}个")
        print(f"奇数一共有{count_odd}个")        
    elif choice == "2":
        print("{n===大小区间分类===")
        for n in nums:
            if n <5:
                print(f"{n}是小数")
                count_small = count_small + 1
            elif n < 8:
                print(f"{n}是中数")
                count_mid = count_mid + 1
            else:
                print(f"{n}是大数")
                count_large = count_large + 1
                print(f"小数有:{count_small}个")
                print(f"中数有:{count_mid}个")
                print(f"大数有:{count_large}个")
    else:
        print("输入错误,请选择1/2/3")
    print("\n==============\n")                       