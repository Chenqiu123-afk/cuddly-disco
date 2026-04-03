import random
# 电脑随机想一个 1-100 的数字
secret_num = random.randint(1, 100)
print("=== 猜数字游戏 ===")
print("我已经想好了 1-100 之间的数字, 来猜吧！")
while True:
    # 让用户输入
    guess = int(input("请输入你猜的数字: "))
    if guess < secret_num:
        print("太小了,在大点! ")
    elif guess > secret_num:
        print("太大了,在小点! ")
    else:
        print("恭喜你,猜对了! 数字就是: ",secret_num)
        break
input("按回车键退出")
