"""
Q1
"""

class Score():
    def __init__(self, mid, final):
        self.mid = mid
        self.final = final


score = Score(50, 75)
print((score.mid + score.final) / 2)


"""
Q2
"""

class Car():
    def __init__(self, fuel, wheels):
        self.fuel = fuel
        self.wheels = wheels

class Bike(Car):
    def __init__(self, fuel, wheels, size):
        super().__init__(fuel, wheels)
        self.size = size

bike = Bike("gas", 2, "small")
print(bike.fuel, bike.wheels, bike.size)


"""
Q3
"""
class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def read_file(self):
        with open(self.file_path, "r") as f:
            for line in f.read().splitlines():
                self.data.append(line.split(","))
        return self.data

filepath = "./data-01-test-score.csv"
read_csv = ReadCSV(filepath)
print(read_csv.read_file())


"""
Q4
"""
class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def read_file(self):
        with open(self.file_path, "r") as f:
            for line in f.read().splitlines():
                self.data.append(line.split(","))
        return self.data

    def merge_list(self):
        csv_file = self.read_file()
        merge_list = [sum(list(map(int, line))) for line in csv_file ]
        return merge_list

read_csv = ReadCSV(filepath)
print(read_csv.read_file())
print(read_csv.merge_list())


"""
Q5
"""
class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def read_file(self):
        with open(self.file_path, "r") as f:
            for line in f.read().splitlines():
                self.data.append(line.split(","))
        return self.data

    def merge_list(self):
        csv_file = self.read_file()
        merge_list = [sum(list(map(int, line)))/len(line) for line in csv_file ]
        return sorted(merge_list)

read_csv = ReadCSV(filepath)
print(read_csv.merge_list())