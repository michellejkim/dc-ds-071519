import pandas as pd
def is_integer(x):
    try:
        _ = int(x)
    except ValueError:
        return False
    return True

sales_df = pd.read_csv('data\EXTR_RPSale.csv')
sales_df = sales_df[['Major', 'Minor', 'DocumentDate', 'SalePrice']]


bldg_df = pd.read_csv('data\EXTR_ResBldg.csv')
bldg_df = bldg_df[['Major', 'Minor', 'SqFtTotLiving', 'ZipCode']]

sales_df['Major'] = pd.to_numeric(sales_df['Major'], errors='coerce')
sales_df['Minor'] = pd.to_numeric(sales_df['Minor'], errors='coerce')
sales_data = pd.merge(sales_df, bldg_df, on=['Major', 'Minor'])


cleaned_data = sales_data.loc[~sales_data['ZipCode'].isna(), :]
print("After filtering for NaN ZipCodes I have {} records".format(len(cleaned_data)))

cleaned_data = cleaned_data.loc[sales_data['SalePrice']>0, :]
print("After filtering for SalePrice I have {} records".format(len(cleaned_data)))

cleaned_data = cleaned_data.loc[cleaned_data['SqFtTotLiving']>0, :]
print("After filtering for SqFt I have {} records".format(len(cleaned_data)))

cleaned_data.loc[cleaned_data['ZipCode'].apply(is_integer) == False, 'ZipCode'].head()
print("After filtering for non-integer ZipCodes I have {} records".format(len(cleaned_data)))

cleaned_data['ZipCode'] = cleaned_data['ZipCode'].map(str)
cleaned_data['ZipCode'] = cleaned_data['ZipCode'].map(lambda x: x[:5])
print("After filtering for ZipCodes Length, I have {} records".format(len(cleaned_data)))

cleaned_data['PricePerSqFt'] = cleaned_data.SalePrice/cleaned_data.SqFtTotLiving

cleaned_data2019 = cleaned_data[cleaned_data['DocumentDate'].map(lambda x: '2019' in x)]
print("After filtering for 2019, I have {} records".format(len(cleaned_data2019)))

zipcodes = [98101, 98102, 98103, 98104, 98105, 98106, 98107, 98108, 98109, 98112, 98115,\
98116, 98117, 98118, 98119, 98121, 98122, 98125, 98126, 98133, 98134, 98136,\
98144, 98146, 98154, 98164, 98174, 98177, 98178, 98195, 98199]
seattle_zips = pd.DataFrame(zipcodes,columns = ['ZipCode'])

seattle_zips = seattle_zips.astype(str)
seattle_property = cleaned_data2019.merge(seattle_zips,on='ZipCode',how = 'inner')
print("After merging to seattle zips, I have {} records".format(len(seattle_property)))

print("Average Price per square foot in Seattle 2019 is $", round(seattle_property.PricePerSqFt.mean(),2))
print("This is based on {} unique records".format(len(seattle_property)))
