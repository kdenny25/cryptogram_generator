import pandas as pd
import os


class importFile():

    def __init__(self, file_path):
        #self.__filepath = file_path
        self.dataframe = self.__gendataframe(file_path)
        self.list = self.__filetolist(self.dataframe)

    # generates dataframe from file_path
    @staticmethod
    def __gendataframe(file_path):
        splitPath = os.path.splitext(file_path)

        # determines whether file is a csv or excel for proper conversion
        if splitPath[1] == '.csv':
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)

        return df

    # converts the file to a list.
    @staticmethod
    def __filetolist(df):

        # selects only the first column in dataframe
        df = df.iloc[:, 0]

        return df.values.tolist()

#p = importFile("C:\\Users\\kdenn\\OneDrive\\My Books\\Puzzle Books\\Cryptogram_V2\\Raw_CSVs\\1990_News.csv")

#print(p.list)