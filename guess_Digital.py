answer = 10
while True:
    num = int(input("猜一个数字（1-100）:"))
    if num == answer:
        print("恭喜你,猜对了! ")
        break
    else:
        print("猜错了,继续")