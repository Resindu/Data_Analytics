import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data =  pd.read_csv('/Users/resindunavoda/Downloads/Sample_Data_for_Activity.csv')
data
data.head(5)
data.info()
sns.displot(data['Normal_Distribution'], kde=True, bins=100)
sns.jointplot(x='Normal_Distribution', y='Exponential_Distribution', data=data, kind='scatter')
sns.jointplot(x='Normal_Distribution', y='Exponential_Distribution', data=data, kind='reg')
sns.jointplot(x='Normal_Distribution', y='Exponential_Distribution', data=data, hue='Poisson_Distribution', kind='kde')