import csv
import random


class Dataset:
    def __init__(self):
        train_data_path = "data/train.csv"
        # test_data_path = "data/test.csv"
        self.train_data, self.gt_train_data = self.read_data(train_data_path)
        print ("Done")

    def read_data(self, path):
        data = []
        gt = []
        with open(path, 'rb') as data_file:
            for row in csv.reader(data_file):
                data.append(self.process_data(row[2:]))
                gt.append(row[1])
        return data, gt

    def process_data(self, row):
        pclass, _, sex, age, sib_sp, parch, _, fare, _, embarked = row
        pclass = self.process_pclass(pclass)
        sex = self.process_sex(sex)
        age = self.process_age(age)
        sib_sp = self.process_sib_sp(sib_sp)
        parch = self.process_parch(parch)
        fare = self.process_fare(fare)
        embarked = self.process_embarked(embarked)

        out = pclass + sex + age + sib_sp + parch + fare + embarked

        return out

    @staticmethod
    def process_pclass(pclass):
        out = [0., 0., 0.]
        out[int(pclass) - 1] = 1.0
        return out

    @staticmethod
    def process_sex(sex):
        if sex == "male":
            return [1., 0.]
        else:
            return [0., 1.]

    @staticmethod
    def process_age(age):
        if age == '':
            return [0.0, 0.0]
        else:
            return [1.0, float(age) / 100.]

    @staticmethod
    def process_sib_sp(sib_sp):
        return [float(sib_sp) / 100.]

    @staticmethod
    def process_parch(parch):
        return [float(parch) / 100.]

    @staticmethod
    def process_fare(fare):
        return [float(fare) / 100.]

    @staticmethod
    def process_embarked(embarked):
        if embarked == "C":
            return [1., 0., 0.]
        elif embarked == "Q":
            return [0., 1., 0.]
        else:
            return [0., 0., 1.]

    @staticmethod
    def get_data(source, batch_size, shuffle=True, offset=0):
        if shuffle:
            random.shuffle(source)
        return source[offset:batch_size+offset]

    def get_train_data(self, batch_size, shuffle=True):
        return self.get_data(self.train_data, batch_size, shuffle)


ds = Dataset()
