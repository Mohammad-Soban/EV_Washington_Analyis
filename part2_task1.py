import pandas as pd 

print("\nThis module tells about How many Categories are there in Our Dataset\n")

df = pd.read_csv('./Data/DataSet_2_vehicle_model.csv') 
# print(df)

category = df.groupby('Electric Vehicle Type')

def printCategories():
    print(f"Total categories in Our Dataset are : {df['Electric Vehicle Type'].nunique()}")
    print("Names of the Categories : \n")
    c = df['Electric Vehicle Type'].unique()
    for i in c:
        print(i)
    print()
    

bev = category.get_group('Battery Electric Vehicle (BEV)')
phev = category.get_group('Plug-in Hybrid Electric Vehicle (PHEV)')

    

def bevCategory():
    print(bev[['Make','Model','Electric Vehicle Type']])
    print()


def phevCategory():
    print(phev[['Make','Model','Electric Vehicle Type']])
    print()



def infoCount():
    print(f"Total No. of vehicles are : {df.shape[0]}\n")
    print(f'Total BEV vehicles are : {bev.shape[0]}\n')
    print(f'Total PHEV vehicles are : {phev.shape[0]}\n')
    return {bev.shape[0] , phev.shape[0]}









def callAllFunction():
    printCategories()
    bevCategory()
    phevCategory()
    infoCount()
    




callAllFunction()


import pandas as pd

def get_vehicle_counts():
    df = pd.read_csv('./Data/DataSet_2_vehicle_model.csv')

    category = df.groupby('Electric Vehicle Type')

    bev = category.get_group('Battery Electric Vehicle (BEV)')
    phev = category.get_group('Plug-in Hybrid Electric Vehicle (PHEV)')

    bev_count = bev.shape[0]
    phev_count = phev.shape[0]

    return bev_count, phev_count
