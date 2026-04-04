# 任务管理系统
tasks = []

# 主程序
while True:
    print("=====================")
    print("欢迎你的到来")
    print("=====================")

    print("1.添加任务")
    print("2.查看所有任务")
    print("3.删除任务")
    print("4.标记完成任务")
    print("5.退出程序")

    # 获取用户选择
    choice = input("请选择功能1/2/3/4/5")

    # 处理用户选择
    if choice == "5":
        print("退出程序")
        break
    # 添加任务
    elif choice == "1":
        task = input("请输入任务内容")
        tasks.append({"task": task, "completed": False})
        print("任务已添加")

    # 判断任务列表是否为空
    elif choice == "2":
        print("\n===所有任务===")
        if not tasks:
            print("没有任务")
        else:
            for idx, task in enumerate(tasks):
                print(f"{idx + 1}. {task['task']}")
    # 删除任务
    elif choice == "3":
        task_num = int(input("请输入要删除的任务编号"))
        if 1 <= task_num <= len(tasks):
            del tasks[task_num - 1]
            print("任务已删除")
        else:
            print("无效的任务编号")
    # 标记完成任务
    elif choice == "4":
        task_num = int(input("请输入要标记完成的任务编号"))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("任务已标记为完成")
        else:
            print("无效的任务编号")

    else:
        print("无效选择，请重新输入。")