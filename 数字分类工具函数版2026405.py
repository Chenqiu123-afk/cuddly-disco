def show_menu():#显示菜单
    print("请选择数字分类工具：")
    print("1. 奇数/偶数分类工具")
    print("2. 小数/中数/大数分类工具")
    print("3. 退出程序")
def get_int_input(prompt):#获取整数输入，并进行错误处理
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("输入错误，请输入一个有效的数字！")
def check_odd_even(nums):#奇数偶数分类工具
        count_odd = 0
        count_even = 0
        for n in nums:
            if n % 2 == 0:
                print(f"{n}是偶数")
                count_even += 1
            else:
                print(f"{n}是奇数")
                count_odd += 1
        print(f"偶数一共有：{count_even}个")
        print(f"奇数一共有：{count_odd}个")
def check_size(nums):#小数中数大数分类工具
        count_small = 0
        count_mid = 0
        count_large = 0
        for n in nums:
            if n < 5:
                print(f"{n}是小数")
                count_small += 1
            elif n < 8:
                print(f"{n}是中数")
                count_mid += 1
            else:
                print(f"{n}是大数")
                count_large += 1
        print(f"小数一共有：{count_small}个")
        print(f"中数一共有：{count_mid}个")
        print(f"大数一共有：{count_large}个")    
while True:#主循环，直到用户选择退出
        show_menu()#显示菜单
        choice = input("请输入选择：")#获取用户选择
        if choice == "3":#用户选择退出
            print("退出程序")# 打印退出信息
            break# 退出循环，结束程序 
        elif choice in ("1", "2"):#用户选择分类工具
            start = get_int_input("请输入开始数字：")# 获取开始数字输入
            end = get_int_input("请输入结束数字：")#    获取结束数字输入
            if start > end:
                print("输入错误，开始数字必须小于或等于结束数字！")
                continue
            nums = list(range(start, end + 1))
            if choice == "1":
                check_odd_even(nums)#调用奇数偶数分类工具
            else:
                check_size(nums)#调用小数中数大数分类工具
        else:
            print("输入错误，请选择1、2或3！")

