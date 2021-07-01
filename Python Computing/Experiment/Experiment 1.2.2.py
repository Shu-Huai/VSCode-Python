inputString = input("请输入 24 小时制的时间，使用格式为“小时：分钟：秒”：")
hour, minute, second = tuple(map(int, inputString.split('：')))
second = second + 1
if second == 60:
    second = 0
    minute = minute + 1
    if minute == 60:
        minute = 0
        hour = hour + 1
        if hour == 24:
            hour = 0
print("一秒后的时间是：" + "%02d" % hour + "：" + "%02d" % minute + "：" + "%02d" % second + "。")