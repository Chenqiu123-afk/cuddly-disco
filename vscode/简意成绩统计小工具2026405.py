while True:
    print("========成绩统计工具========")
    print("输入多个成绩，用空格分隔，按" "Enter" "键结束输入")
    input_str = input("请输入成绩: ")
    if not input_str:
        print("没有输入成绩，请重新输入！")
        continue
    else:
        scores = list(map(float, input_str.split()))
        total = sum(scores)
        average = total / len(scores)   
        print(f"总成绩: {total:.2f}")
        print(f"平均成绩: {average:.2f}")
        break
    