class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False
    def __call__(self, x):
        if x in self.group:
            print("変更された！")
            self.found = True
            return(0,x)
        return (1,x)

numbers = [8, 4, 1, 2, 5, 4, 7, 6]
group = [2, 3, 5, 7]

sorter = Sorter(group)
print("sorterインスタンス化した後")
numbers.sort(key = sorter) #これの実行時に__call__が呼ばれるっぽい
print("sort呼び出した後")
print(sorter.found)
print(numbers)
