import pandas as pd
df = pd.read_csv('./Data/DataSet_2_vehicle_model.csv')

def listOfElectricityProvider():
    count = 0
    list_of_provider = df['Electric Utility'].unique()
    for i in list_of_provider:
        print(i)
        count += 1
    print(f"\nTotal Electricity Providers are : {count}\n")

def electricityProviderCount():
    electricity_provider_count = df.groupby(['Electric Utility', 'County']).size().reset_index(name='Count')
    print(electricity_provider_count)

def callAllFunction():
    listOfElectricityProvider()
    electricityProviderCount()

callAllFunction()
