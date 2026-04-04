# 学生成绩管理系统
students = {}
# 程序
while True:
    print("=====================")
    print("欢迎你的到来")
    print("=====================")
    print("1.添加学生成绩(输入学生姓名和成绩)")
    print("2.查看所有学生成绩")
    print("3.删除学生成绩")
    print("4.退出程序")
    # 获取用户选择
    choice = input("请选择功能1/2/3/4")
    # 处理用户选择
    if choice == "4":
        print("退出程序")
        break
    # 添加学生成绩
    elif choice == "1":
        name = input("请输入学生姓名")
        score = input("请输入学生成绩")
        students[name] = score
        print("学生成绩已添加")
    # 查看所有学生成绩
    elif choice == "2":
        print("\n===所有学生成绩===")
        if not students:
            print("没有学生成绩")
        else:
            for name, score in students.items():
                print(f"姓名: {name} 成绩: {score}")
    # 删除学生成绩
    elif choice == "3":
        name = input("请输入要删除的学生姓名")
        if name in students:
            del students[name]
            print("学生成绩已删除")
        else:
            print("无效的学生姓名")