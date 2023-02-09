import pandas as pd
import glob
import os

column_rain = 'Total Rain (mm)'
column_snow = 'Total Snow (cm)'
column_precip = 'Total Precip (mm)'
target_column = column_rain

path_data = r'./data/' # use your path
all_files_trt = glob.glob(os.path.join(path_data, "toronto/*.csv"))
all_files_van = glob.glob(os.path.join(path_data, "vancouver/*.csv"))

df_trt = pd.concat((pd.read_csv(f) for f in all_files_trt), ignore_index=True)
df_van = pd.concat((pd.read_csv(f) for f in all_files_van), ignore_index=True)

df_trt.fillna(0, inplace=True)
df_van.fillna(0, inplace=True)

df_trt_sum = df_trt.groupby(by='Year')[target_column].sum()
df_trt_mean = df_trt.groupby(by='Year')[target_column].mean()
df_van_sum = df_van.groupby(by='Year')[target_column].sum()
df_van_mean = df_van.groupby(by='Year')[target_column].mean()

df_diff_sum = df_van_sum - df_trt_sum

df_trt_sum_monthly = df_trt.groupby(['Year', 'Month'])[target_column].sum()
df_van_sum_monthly = df_van.groupby(['Year', 'Month'])[target_column].sum()

df_trt_sum_monthly.to_csv('./results/trt_sum_monthly.csv', sep='\t')
df_van_sum_monthly.to_csv('./results/van_sum_monthly.csv', sep='\t')

print("Toronto annual {} mean:".format(target_column))
print(df_trt_sum.mean())
print("Toronto annual {} sum:".format(target_column))
print(df_trt_sum)

print()
print("Vancouver annual {} mean:".format(target_column))
print(df_van_sum.mean())
print("Vancouver annual {} sum:".format(target_column))
print(df_van_sum)

print()
print("Difference between Vancouver and Toronto annual {} mean:".format(target_column))
print(df_diff_sum.mean())
print("Difference between Vancouver and Toronto annual {} sum:".format(target_column))
print(df_diff_sum)

print()
print("Vancouver over Toronto {} mean".format(target_column), df_van_sum.mean() / df_trt_sum.mean())
print("Toronto over Vancouver {} mean".format(target_column), df_trt_sum.mean() / df_van_sum.mean())
