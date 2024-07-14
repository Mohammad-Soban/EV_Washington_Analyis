import pandas as pd

print("\nThis module tells which category of EV is sold most\n")

df = pd.read_csv('./Data/DataSet_2_vehicle_model.csv')

def categoriesCountBrandWise():
    df = pd.read_csv('./Data/DataSet_2_vehicle_model.csv')
    category = df.groupby(['Make', 'Electric Vehicle Type']).size().reset_index(name='Count')

    # Pivot the category DataFrame to have Electric Vehicle Types as columns and their counts as values
    pivot_df = category.pivot(index='Make', columns='Electric Vehicle Type', values='Count').reset_index()

    # Fill NaN values with 0
    pivot_df.fillna(0, inplace=True)

    return pivot_df
    
    
categoriesCountBrandWise()