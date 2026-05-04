import matplotlib.pyplot as plt

def survival_count(df):
    df['Survived'].value_counts().plot(kind='bar')
    plt.title("Survival Count")
    plt.xlabel("Survived (0 = No, 1 = Yes)")
    plt.ylabel("Count")
    plt.show()

def survival_by_gender(df):
    df.groupby(['Sex', 'Survived']).size().unstack().plot(kind='bar')
    plt.title("Survival by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.legend(["Not Survived", "Survived"])
    plt.show()

def class_distribution(df):
    df['Pclass'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Passenger Class Distribution")
    plt.ylabel("")
    plt.show()

def age_distribution(df):
    df['Age'].hist(bins=20)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()

def fare_vs_class(df):
    df.boxplot(column='Fare', by='Pclass')
    plt.title("Fare vs Passenger Class")
    plt.xlabel("Class")
    plt.ylabel("Fare")
    plt.show()

# Call functions
survival_count(df)
survival_by_gender(df)
class_distribution(df)
age_distribution(df)
fare_vs_class(df)