import pandas as pd
import numpy as np

class univariate():

    @staticmethod
    def quanQual(dataset):
        quan = []
        qual = []
        for columnname in dataset.columns:
            if dataset[columnname].dtype == 'O':
                qual.append(columnname)
            else:
                quan.append(columnname)
        return quan, qual

    @staticmethod
    def freqtable(columnName, dataset):
        freqtable = pd.DataFrame(columns=["unique_values", "Frequency", "Relative Frequency", "custom"])
        freqtable["unique_values"] = dataset[columnName].value_counts().index
        freqtable["Frequency"] = dataset[columnName].value_counts().values
        freqtable["Relative Frequency"] = freqtable["Frequency"] / len(dataset)
        freqtable["custom"] = freqtable["Relative Frequency"].cumsum()
        return freqtable

    @staticmethod
    def univariate(dataset, quan):
        descriptive = pd.DataFrame(
            index=["mean", "Median", "Mode", "Q1:25%", "Q2:50%",
                   "Q3:75%", "99", "Q4:100", "IQR", "1.5rule",
                   "Lesser", "Greater", "Min", "Max", "kurtosis", "skew"],
            columns=quan
        )

        for columnName in quan:
            descriptive.loc["mean", columnName] = dataset[columnName].mean()
            descriptive.loc["Median", columnName] = dataset[columnName].median()
            descriptive.loc["Mode", columnName] = dataset[columnName].mode()[0]
            descriptive.loc["Q1:25%", columnName] = dataset[columnName].quantile(0.25)
            descriptive.loc["Q2:50%", columnName] = dataset[columnName].quantile(0.50)
            descriptive.loc["Q3:75%", columnName] = dataset[columnName].quantile(0.75)
            descriptive.loc["Q4:100", columnName] = dataset[columnName].max()
            descriptive.loc["99", columnName] = np.percentile(dataset[columnName], 99)
            descriptive.loc["IQR", columnName] = descriptive.loc["Q3:75%", columnName] - descriptive.loc["Q1:25%", columnName]
            descriptive.loc["1.5rule", columnName] = 1.5 * descriptive.loc["IQR", columnName]
            descriptive.loc["Lesser", columnName] = descriptive.loc["Q1:25%", columnName] - descriptive.loc["1.5rule", columnName]
            descriptive.loc["Greater", columnName] = descriptive.loc["Q3:75%", columnName] + descriptive.loc["1.5rule", columnName]
            descriptive.loc["Min", columnName] = dataset[columnName].min()
            descriptive.loc["Max", columnName] = dataset[columnName].max()
            descriptive.loc["kurtosis", columnName] = dataset[columnName].kurtosis()
            descriptive.loc["skew", columnName] = dataset[columnName].skew()
        return descriptive

    @staticmethod
    def lesserGreater(quan,descriptive):
        lesser = []
        greater = []
        for col in quan:
            if descriptive.loc["Min", col] < descriptive.loc["Lesser", col]:
                lesser.append(col)
            if descriptive.loc["Max", col] > descriptive.loc["Greater", col]:
                greater.append(col)
        return lesser, greater

    @staticmethod
    def outlierfix(dataset, descriptive, lesser, greater):
        for col in lesser:
            dataset.loc[dataset[col] < descriptive.loc["Lesser", col], col] = descriptive.loc["Lesser", col]
        for col in greater:
            dataset.loc[dataset[col] > descriptive.loc["Greater", col], col] = descriptive.loc["Greater", col]
        return dataset
