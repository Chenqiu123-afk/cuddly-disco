# 备忘录（学习版）
Memo = {} # 用于存储备忘录的字典
# 主程序
while True:
    print("欢迎使用备忘录！")# 功能菜单
    print("1. 添加备忘录")
    print("2. 查看备忘录")
    print("3. 删除备忘录")
    print("4. 退出")
    choice = input("请输入您的选择（1-4）：")
    if choice == "4":# 退出程序
        print("感谢使用备忘录，再见！")
        break
    elif choice == "1":# 添加备忘录
        title = input("请输入备忘录标题：")
        content = input("请输入备忘录内容：")
        Memo[title] = content
        print("备忘录已添加！")
    elif choice == "2":# 查看备忘录
        if not Memo:
            print("没有备忘录！")
        else:
            print("备忘录列表：")
            for title, content in Memo.items():
                print(f"标题：{title}，内容：{content}")
    elif choice == "3":# 删除备忘录
        title == input("请输入要删除的备忘录标题：")
        if title in Memo:
            del Memo[title]
            print("备忘录已删除！")
        else:            
            print("没有找到该备忘录！")
    else:
        print("无效的选择，请重新输入！")        




