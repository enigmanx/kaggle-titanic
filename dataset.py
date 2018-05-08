import csv


class Dataset:
    def __init__(self):
        train_data_path = "data/train.csv"
        test_data_path = "data/test.csv"
        self.train_data = self.read_data(train_data_path)
        self.test_data = self.read_data(test_data_path)

    @staticmethod
    def read_data(path):
        data = []
        with open(path, 'rb') as data_file:
            for row in csv.reader(data_file):
                data.append(row)
        return data

ds = Dataset()
