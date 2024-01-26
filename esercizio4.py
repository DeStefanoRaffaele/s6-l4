import seaborn as sns 
titanic = sns.load_dataset('titanic')
from matplotlib import pyplot as plt

print(titanic)

#Quanti ponti c'erano sulla nave?
count_data = titanic['deck'].value_counts()
print(count_data)

#somma e restituisce l'indice dove risultano dati nulli
missing_data = titanic.isnull().sum()
print(missing_data)

sns.lmplot(data = titanic, x="age", y="fare")
plt.show()