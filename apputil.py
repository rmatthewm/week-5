import plotly.express as px
import pandas as pd

# update/add code below ...

# Read in the Titanic data
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

def survival_demographics():
    """ Return a dataframe with the survival information for each combination 
    of class, age group and gender.

    Returns:
        pandas.Dataframe: the dataframe with the data
    """

    # For now we will just do this
    global df

    # Choosing the last age as 200 to include all people 60+
    df['age_group'] = pd.cut(df['Age'], bins=[0,13,20,60,200], labels=['Child', 'Teen', 'Adult', 'Senior'])

    # Since we only care about the statistics for each group, we can aggregate
    # the data with the number of passengers and survivors
    results_table = df.groupby(['Pclass', 'age_group', 'Sex'], observed=True).agg({'PassengerId': 'count', 'Survived': 'sum'})

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

