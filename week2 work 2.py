class Median:
    def __init__(self):
        self.targets = []

    def get_item(self, item):
        self.targets.append(item)

    def clear(self):
        self.targets=[]

    def show_result(self):
        self.idx=0
        self.targets.sort()
        if len(self.targets)%\
                2==0:
            self.idx=len(self.targets)//2
            self.a=self.targets[self.idx-1]+self.targets[self.idx]
            print(self.a/2)
        else:
            self.idx=len(self.targets)//2
            print(self.targets[self.idx])



median = Median()
for x in range(10):
    median.get_item(x)
median.show_result()

median.clear()
for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
    median.get_item(x)
median.show_result()