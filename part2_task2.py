import pandas as pd 
import plotly.express as px

print("\nThis module tells How many Cars in WA Companywise\n")

df = pd.read_csv('./Data/DataSet_2_vehicle_model.csv')
# print(df)

counties = df.groupby('County')

def allCounties():
    count = 0
    list_of_counties = df['County'].unique()
    for i in list_of_counties:
        print(i)
        count += 1
    print(f"\nTotal Counties in WA are : {count}\n")


def allCitiesInCounties():
    for i,j in counties:
        print(f"County Name : {i}")
        print(j[['County', 'City']])
        print()
    

def CarsCountyWise():
    df = pd.read_csv('./Data/DataSet_2_vehicle_model.csv')
    grouped_data = df.groupby(['County', 'Make']).size().reset_index(name='Count')

    # Plotting using Plotly
    fig = px.bar(grouped_data, x='Make', y='Count', color='County',
                 labels={'Count': 'Number of Cars', 'Make': 'Car Company (Make)', 'County': 'County'},
                 title='Number of Cars in Each County Company-wise')
    fig.update_xaxes(tickangle=45)
    
    # Instead of fig.show(), return the figure object
    return fig  
    

def CarsCityWise():
    grouped_data = df.groupby(['County', 'City', 'Make']).size().reset_index(name='Count')

    print("\nNumber of Cars in each County, City, Company wise:\n")
    print(grouped_data)
    
    print(f"\nTotal Count of Cars : {grouped_data['Count'].sum()}\n")


def allCompanies():
    count = 0
    list_of_company = df['Make'].unique()
    for i in list_of_company:
        print(i)
        count += 1
    print(f"\nTotal Companies are : {count}\n")
    

def totalCars():
    company = df.groupby('Make')
    list = []
    for i,j in company:
        # print(i)
        # print(f"Total Cars of {i} company is : {j.shape[0]}\n")
        list.append([i,j.shape[0]])
    print("List started")
    print(list)
    print("List end")
    return list


def callAllFunction():
    allCompanies()
    totalCars()
    allCounties()
    CarsCountyWise()
    # allCitiesInCounties()
    # CarsCityWise()


callAllFunction()


def get_car_data():
    df = pd.read_csv('./Data/DataSet_2_vehicle_model.csv')

    # Your existing functions here

    # For example, returning the list of total cars per company
    company = df.groupby('Make')
    car_list = []
    for make, group_df in company:
        car_list.append([make, group_df.shape[0]])

    return car_list