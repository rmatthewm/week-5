import plotly.express as px
import pandas as pd

# update/add code below ...

# Read in the Titanic data
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

def survival_demographics():
    # For now we will just do this
    global df

    # Choosing the last age as 200 to include all people 60+
    df['age_group'] = pd.cut(df['Age'], bins=[0,13,20,60,200], labels=['Child', 'Teen', 'Adult', 'Senior'])

    # Add the number of passengers in that group
    df['n_passengers'] = df.groupby(['Pclass', 'age_group', 'Sex'])['PassengerId'].transform('count')

    # Add up the number of survivors in that group, we can use sum since survived is 0 or 1
    df['n_survivors'] = df.groupby(['Pclass', 'age_group', 'Sex'])['Survived'].transform('sum')

    # Add the survival rate
    df['survival_rate'] = df['n_survivors'] / df['n_passengers']

    return df[['Pclass', 'Sex', 'age_group', 'n_passengers', 'n_survivors', 'survival_rate']]


print(survival_demographics().head())