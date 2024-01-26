import seaborn as sns 
titanic = sns.load_dataset('titanic')
from matplotlib import pyplot as plt

# numero di passeggeri di ogni classe di imbarco
sns.countplot(x='class', data=titanic) #countplot conta i dati univoci
plt.xlabel("Classe di Imbarco")
plt.ylabel("Numero di Passeggeri")
plt.show()

# numero di sopravvisuti di ogni classe di imbarco
sns.countplot(x='alive', data=titanic)
plt.xlabel("Sopravvissuti")
plt.ylabel("Numero di Passeggeri")
plt.show()

#distribuzione delle età dei passeggeri rispetto alla classe di imbarco boxplot
sns.boxplot(x="class", y="age", data=titanic)
plt.xlabel("Classe")
plt.ylabel("Età")
plt.show()

#distribuzione delle età dei passeggeri rispetto alla classe di imbarco swarmplot
sns.swarmplot(x="class", y="age", data=titanic)
plt.xlabel("Classe")
plt.ylabel("Età")
plt.show()

#colonne fare e survived boxplot
sns.boxplot(x="survived", y="fare", data=titanic)
plt.xlabel("Sopravvisuti")
plt.ylabel("Tariffa")
plt.show()

##colonne fare e survived swarmplot
sns.swarmplot(x="survived", y="fare", data=titanic)
plt.xlabel("Sopravvissuti")
plt.ylabel("Tariffa")
plt.show()
