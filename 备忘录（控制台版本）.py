# 备忘录（控制台版本）
Memo = {}  # 用于存储备忘录的字典

# 主程序
while True:
    print("=====================")
    print("欢迎你的到来")
    print("=====================")

    print("1.添加备忘录")
    print("2.查看所有备忘录")
    print("3.删除备忘录")
    print("4.退出程序")

    # 获取用户选择
    choice = input("请选择功能1/2/3/4")

    # 处理用户选择
    if choice == "4":
        print("退出程序")
        break
    # 添加备忘录
    elif choice == "1":
        title = input("请输入备忘录标题")
        content = input("请输入备忘录内容")
        Memo[title] = content
        print("备忘录已添加")

    # 判断备忘录是否为空
    elif choice == "2":
        print("\n===所有备忘录===")
        if not Memo:
            print("没有备忘录")
        else:
            for title, content in Memo.items():
                print(f"标题: {title} 内容: {content}")
    # 删除备忘录
    elif choice == "3":
        title = input("请输入要删除的备忘录标题")
        if title in Memo:
            del Memo[title]
            print("备忘录已删除")
        else:
            print("无效的备忘录标题")

    else:
        print("无效选择，请重新输入。")