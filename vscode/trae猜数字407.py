import random

def number_guessing_game():
    """数字猜谜游戏"""
    print("欢迎来到数字猜谜游戏！")
    print("我已经想好了一个1到100之间的数字，你需要猜出来。")
    print("每次猜测后，我会告诉你是猜大了还是猜小了。")
    print("看看你需要多少次才能猜对！\n")
    
    # 生成1-100之间的随机数
    target_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # 获取用户输入
            guess = int(input("请输入你的猜测（1-100）："))
            attempts += 1
            
            # 检查猜测是否在有效范围内
            if guess < 1 or guess > 100:
                print("请输入1到100之间的数字！")
                continue
            
            # 比较猜测与目标数字
            if guess < target_number:
                print("猜小了！再试一次。")
            elif guess > target_number:
                print("猜大了！再试一次。")
            else:
                print(f"恭喜你猜对了！目标数字就是{target_number}。")
                print(f"你总共用了{attempts}次尝试。")
                break
        except ValueError:
            print("请输入有效的数字！")

if __name__ == "__main__":
    number_guessing_game()
