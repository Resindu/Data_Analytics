import seaborn as sns
import matplotlib.pyplot as plt
titanic = sns.load_dataset('titanic')

sns.jointplot(x='fare', y='age', data=titanic, kind='scatter')
sns.displot(titanic['fare'], kde=False, bins=100)
sns.boxplot(x = 'class', y = 'age', data = titanic)
sns.boxplot(x = 'class', y = 'age', data = titanic,palette='Set1',hue='class')
sns.countplot(x='sex',data=titanic)
corr_matrix = titanic.select_dtypes(include=["number"]).corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)