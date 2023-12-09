import pandas as pd
df = pd.read_csv('dataset-1.csv')
def generate_car_matrix(data):
    result_df = data.pivot(index='id_1', columns='id_2', values='car')
    result_df.fillna(0, inplace=True)  
    result_df.values[[range(len(result_df))], [range(len(result_df))]] = 0  
    return result_df
new_df = generate_car_matrix(df)
print(new_df)
