class Time(object):
    def __init__(self, hour=0, minute=0, second=0) -> None:
        super().__init__()
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "%02d:%02d:%02d" % (self.hour, self.minute, self.second)

    def __add__(self, time):
        hour = self.hour + time.hour
        minute = self.minute + time.minute
        second = self.second + time.second
        if second >= 60:
            second -= 60
            minute += 1
        if minute >= 60:
            minute -= 60
            hour += 1
        if hour >= 24:
            hour -= 24
        return Time(hour, minute, second)

    def TimeToInt(self):
        return self.second + 60 * self.minute + 3600 * self.hour

    def PrintTime(self):
        print("Time is: %02d:%02d:%02d." % (self.hour, self.minute, self.second))

    def IsAfter(self, time):
        if self.TimeToInt() > time.TimeToInt():
            return True
        return False

    def Increment(self, incrementSecond):
        if incrementSecond <= 0:
            return self
        hour = self.hour
        minute = self.minute
        second = self.second
        second += incrementSecond
        minute += second // 60
        second = second % 60
        hour += minute // 60
        minute = minute % 60
        hour = hour % 24
        return Time(hour, minute, second)

    def IsValid(self):
        if self.hour >= 24 or self.hour < 0 or self.minute >= 60 or self.minute < 0 or self.second >= 60 or self.second < 0:
            return False
        return True


nowTime = Time(0, 1, 30)
print("Time is: %s." % nowTime)
print("Time + 00:00:30 = %s." % (nowTime + Time(0, 0, 30)))
print("Convert to second: %ds." % nowTime.TimeToInt())
nowTime.PrintTime()
print("Time is after 00:00:30:", nowTime.IsAfter(Time(0, 0, 30)))
print("Time after 120s is: %s." % nowTime.Increment(120))
print("Time is valid:", nowTime.IsValid())