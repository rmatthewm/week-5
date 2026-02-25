import plotly.express as px
import pandas as pd

# update/add code below ...

# Read in the Titanic data
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

def survival_demographics():
    """ Return a dataframe with the survival information for each combination 
    of class, age group and gender.

    Returns:
        pandas.DataFrame: the dataframe with the data
    """

    # For now we will just do this
    global df

    df_survival = df.copy()

    # Choosing the last age as 200 to include all people 60+
    df_survival['age_group'] = pd.cut(df['Age'], bins=[0,13,20,60,200], labels=['Child', 'Teen', 'Adult', 'Senior'])

    # Since we only care about the statistics for each group, we can aggregate
    # the data with the number of passengers and survivors
    results_table = df_survival.groupby(['Pclass', 'age_group', 'Sex'], observed=True).agg({'PassengerId': 'count', 'Survived': 'sum'})

    # Reset the index so that we still have Pclass, age_grouop, and Sex as columns
    results_table = results_table.reset_index()

    # We can rename the columns to match the requirements
    results_table = results_table.rename(columns={'PassengerId': 'n_passengers', 'Survived': 'n_survivors'})

    # Calculate the survival rate
    results_table['survival_rate'] = results_table['n_survivors'] / results_table['n_passengers']

    # Return the result sorted by survival rate
    return results_table.sort_values('survival_rate', ascending=False)


def visualize_demographic():
    demographic_df = survival_demographics()

    return px.histogram(demographic_df, 
             x='survival_rate', 
             y='age_group',
             histfunc='avg',
             template='plotly_white',
             color_discrete_sequence=px.colors.qualitative.D3
            )

def family_groups():
    """ Return a dataframe with fare information for each group of passengers

    Returns:
        pandas.DataFrame: the dataframe
    """
    global df

    df_family = df.copy()
    df_family['family_size'] = df_family['SibSp'] + df_family['Parch'] + 1

    # Print this just so we can compare it to last_names()
    print(df_family.sort_values('family_size')['family_size'].value_counts())

    # Create a new aggregate dataframe grouped by class and family size
    # By doing the agg this way we can make separate columns based on Fare
    results_table = df_family.groupby(['Pclass', 'family_size'], observed=True).agg(
        n_passengers=('PassengerId', 'count'), avg_fare=('Fare', 'mean'), 
        min_fare=('Fare', 'min'), max_fare=('Fare', 'max'))

    # Reset the index
    results_table = results_table.reset_index()

    # Sort the result by class and family size
    return results_table.sort_values(['Pclass', 'family_size'])

def last_names():
    """ Returns a series with the count of each unique last name

    Returns:
        pandas.Series: the series of last name counts
    """
    global df

    # Return the number of unique last names by getting the name before the comma
    return df['Name'].str.split(',').str[0].value_counts().sort_values()

def visualize_families():
    df_family = family_groups()

    return px.histogram(df_family, 
             x='family_size', 
             y='avg_fare',
             histfunc='avg',
             template='plotly_white',
             color_discrete_sequence=px.colors.qualitative.D3
            )

# Run just to compare
if __name__ == "__main__":
    family_groups()
    names = last_names()
    print(names.value_counts())