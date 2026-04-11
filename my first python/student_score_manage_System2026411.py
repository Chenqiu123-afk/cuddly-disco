def AddStudent(students):# 添加学生
    print("添加学生")
    id = len(students) + 1
    name = input("请输入学生姓名：")
    try:
        score1 = int(input("请输入第一门成绩："))
        score2 = int(input("请输入第二门成绩："))
        if 0 <= score1 <= 100 and 0 <= score2 <= 100:
            students.append([id, name, score1, score2])
            print(f"学生{id}添加成功！")
        else:
            print("成绩必须在0到100之间！")
    except ValueError:
        print("输入的成绩无效，请输入数字！")

def DeleteStudent(students):# 删除学生
    print("删除学生")
    try:
        id = int(input("请输入学生ID："))
        found = False
        for s in students:
            if s[0] == id:
                students.remove(s)
                found = True
                print(f"学生{id}删除成功！")
                # 更新后续学生的ID
                for i in range(len(students)):
                    students[i][0] = i + 1
                break
        if not found:
            print("未找到该学生")
    except ValueError:
        print("请输入有效的学生ID！")

def queryStudent(students):# 查询学生
    print("查询学生")
    name = input("请输入学生姓名：")
    found = False
    for s in students:
        if s[1] == name:
            print(f"学生{name}的成绩：第一门{s[2]}，第二门{s[3]}")
            found = True
            break
    if not found:
        print("未找到该学生")

def displayAllStudents(students):# 显示所有学生
    print("显示所有学生")
    if not students:
        print("暂无学生信息")
    else:
        print("ID\t姓名\t第一门\t第二门")
        for s in students:
            print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}")

def statistics(students):# 统计学生成绩
    print("统计学生成绩")
    name = input("请输入学生姓名：")
    found = False
    for s in students:
        if s[1] == name:
            total = s[2] + s[3]
            average = total / 2
            print(f"{name}的总成绩是：{total}")
            print(f"{name}的平均成绩是：{average}")
            found = True
            break
    if not found:
        print("未找到该学生")

def saveToFile(students):# 保存学生信息到文件
    print("保存学生信息到文件")
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s[1]},{s[2]},{s[3]}\n")
    print("保存成功！")

def loadFromFile():# 从文件加载学生信息
    print("从文件加载学生信息")
    students = []
    try:
        with open("students.txt", "r") as f:
            for i, line in enumerate(f, 1):
                name, score1, score2 = line.strip().split(",")
                students.append([i, name, int(score1), int(score2)])
        print("加载成功！")
    except FileNotFoundError:
        print("文件未找到，正在创建新文件...")
    return students            

def exitProgram():# 退出程序
    print("退出程序")
    return True

students = loadFromFile()# 初始化学生列表

while True:# 主循环
    print("=====================")
    print("1.添加学生")
    print("2.删除学生")
    print("3.查询学生")
    print("4.显示所有学生")
    print("5.统计学生成绩")
    print("6.保存学生信息到文件")
    print("7.从文件加载学生信息")
    print("8.退出程序")
    choice = input("请输入你的选择（1-8）：")
    if choice == "1":
        AddStudent(students)
    elif choice == "2":
        DeleteStudent(students)
    elif choice == "3":
        queryStudent(students)
    elif choice == "4":
        displayAllStudents(students)
    elif choice == "5":
        statistics(students)
    elif choice == "6":
        saveToFile(students)
    elif choice == "7":
        students = loadFromFile()
    elif choice == "8":
        if exitProgram():
            break
    else:
        print("无效的选择，请重新输入！")