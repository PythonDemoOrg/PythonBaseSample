"""--- 第一个小游戏 --- """
temp = input("不妨猜下小甲鱼心里想的是那个数字：")
guess = int(temp)
if guess == 8:
    print("你是小甲鱼心里的蛔虫吗？！")
    print("哼，猜中了也没有奖励")
else:
    print("猜错了，是8啦！")
print("游戏结束，不玩啦^_^")