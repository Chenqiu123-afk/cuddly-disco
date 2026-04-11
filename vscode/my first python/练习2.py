while True:# 无限循环，直到用户选择退出
    print("=====================")
    input_num = input("请输入一个数字：")# 获取用户输入
    if input_num == "0":# 用户选择退出
        print("退出程序")
        break
    else:
        try:# 尝试将输入转换为整数
            num = int(input_num)
            print(f"你输入的数字是：{num}")
        except ValueError:# 捕获转换错误
            print("输入错误，请输入一个有效的数字！")