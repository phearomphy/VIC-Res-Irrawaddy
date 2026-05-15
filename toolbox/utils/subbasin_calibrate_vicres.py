# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 17:40:35 2025

@author: Phearom
"""

import pandas as pd

# Define file paths
"""
file1 is excel file containing grid locations for each subbasin
file2 is soil file to be modified
change the example file paths accordingly
"""
file1 = "subbasin_calibrate.xlsx"
file2 = "/home/phearom/VIC-Res-Irrawaddy/rainfall_runoff/parameters/soilparam.txt"
output_file = "/home/phearom/VIC-Res-Irrawaddy/rainfall_runoff/parameters/soilpar_30n51n.txt"

# Read sheets representing subbasins from the first file.
# Each sheet must have columns named 'lat' and 'lon'
df_hkamti = pd.read_excel(file1, sheet_name="Hkamti")
df_mawlaik = pd.read_excel(file1, sheet_name="Mawlaik")
df_monywa = pd.read_excel(file1, sheet_name="Monywa")
df_katha = pd.read_excel(file1, sheet_name="Katha")
df_sagaing = pd.read_excel(file1, sheet_name="Sagaing")
df_magway = pd.read_excel(file1, sheet_name="Magway")
df_pyay = pd.read_excel(file1, sheet_name="Pyay")

# Create coordinate tuples for lookup
hkamti_coords = set(zip(df_hkamti['lat'], df_hkamti['lon']))
mawlaik_coords = set(zip(df_mawlaik['lat'], df_mawlaik['lon']))
monywa_coords = set(zip(df_monywa['lat'], df_monywa['lon']))
katha_coords = set(zip(df_katha['lat'], df_katha['lon']))
sagaing_coords = set(zip(df_sagaing['lat'], df_sagaing['lon']))
magway_coords = set(zip(df_magway['lat'], df_magway['lon']))
pyay_coords = set(zip(df_pyay['lat'], df_pyay['lon']))

# Read the second file
df_soilpar = pd.read_csv(file2, sep='\t')

# Create boolean masks for df_soilpar
# In df_soilpar, the lat is in column index 2 and lon in column index 3.
hkamti_mask = df_soilpar.apply(lambda row: (row[2], row[3]) in hkamti_coords, axis=1)
mawlaik_mask = df_soilpar.apply(lambda row: (row[2], row[3]) in mawlaik_coords, axis=1)
monywa_mask = df_soilpar.apply(lambda row: (row[2], row[3]) in monywa_coords, axis=1)
katha_mask = df_soilpar.apply(lambda row: (row[2], row[3]) in katha_coords, axis=1)
sagaing_mask = df_soilpar.apply(lambda row: (row[2], row[3]) in sagaing_coords, axis=1)
magway_mask = df_soilpar.apply(lambda row: (row[2], row[3]) in magway_coords, axis=1)
pyay_mask = df_soilpar.apply(lambda row: (row[2], row[3]) in pyay_coords, axis=1)

# For overlapping coordinates
# hkamti
df_soilpar.loc[hkamti_mask, 4] = 0.4        #INFILT = 0.4 (config 30n18)
df_soilpar.loc[hkamti_mask, 5] = 0.9        #Ds = 0.9 (config 30n18)
df_soilpar.loc[hkamti_mask, 6] = 7.167      #Ds_MAX = 7.167 (config 30n18)
df_soilpar.loc[hkamti_mask, 7] = 1          #Ws = 1 (config 30n18)
df_soilpar.loc[hkamti_mask, 18] = 0.5       #DEPTH_1 = 0.3 (config 30n18)
df_soilpar.loc[hkamti_mask, 19] = 0.7       #DEPTH_2 = 0.7 (config 30n18)

# mawlaik
df_soilpar.loc[mawlaik_mask, 4] = 0.4       #INFILT = 0.4 (config 30n18)
df_soilpar.loc[mawlaik_mask, 5] = 0.9       #Ds = 0.9 (config 30n18)
df_soilpar.loc[mawlaik_mask, 6] = 7.167     #Ds_MAX = 7.167 (config 30n18)
df_soilpar.loc[mawlaik_mask, 7] = 1         #Ws = 1 (config 30n18)
df_soilpar.loc[mawlaik_mask, 18] = 0.5      #DEPTH_1 = 0.3 (config 30n18)
df_soilpar.loc[mawlaik_mask, 19] = 0.7      #DEPTH_2 = 0.7 (config 30n18)

# monywa
df_soilpar.loc[monywa_mask, 4] = 0.4        #INFILT = 0.4 (config 30n18)
df_soilpar.loc[monywa_mask, 5] = 0.9        #Ds = 0.9 (config 30n18)
df_soilpar.loc[monywa_mask, 6] = 7.167      #Ds_MAX = 7.167 (config 30n18)
df_soilpar.loc[monywa_mask, 7] = 1          #Ws = 1 (config 30n18)
df_soilpar.loc[monywa_mask, 18] = 0.5       #DEPTH_1 = 0.3 (config 30n18)
df_soilpar.loc[monywa_mask, 19] = 0.7       #DEPTH_2 = 0.7 (config 30n18)

# katha
df_soilpar.loc[katha_mask, 4] = 0.5         #INFILT = 0.4 (config 30n18)
df_soilpar.loc[katha_mask, 5] = 0.59        #Ds = 0.9 (config 30n18)
df_soilpar.loc[katha_mask, 6] = 7           #Ds_MAX = 10 (config 30n18)
df_soilpar.loc[katha_mask, 7] = 0.60        #Ws = 0.6 (config 30n18)
df_soilpar.loc[katha_mask, 18] = 0.1        #DEPTH_1 = 0.2 (config 30n18)
df_soilpar.loc[katha_mask, 19] = 1.2        #DEPTH_2 = 0.8 (config 30n18)

# sagaing
df_soilpar.loc[sagaing_mask, 4] = 0.4       #INFILT = 0.4 (config 30n18)
df_soilpar.loc[sagaing_mask, 5] = 0.3       #Ds = 0.9 (config 30n18)
df_soilpar.loc[sagaing_mask, 6] = 10        #Ds_MAX = 10 (config 30n18)
df_soilpar.loc[sagaing_mask, 7] = 0.6       #Ws = 0.6 (config 30n18)
df_soilpar.loc[sagaing_mask, 18] = 0.3      #DEPTH_1 = 0.3 (config 30n18)
df_soilpar.loc[sagaing_mask, 19] = 0.7      #DEPTH_2 = 0.7 (config 30n18)

# magway
df_soilpar.loc[magway_mask, 4] = 0.6        #INFILT = 0.6 (config 30n18)
df_soilpar.loc[magway_mask, 5] = 0.9        #Ds = 0.9 (config 30n18)
df_soilpar.loc[magway_mask, 6] = 2          #Ds_MAX = 2 (config 30n18)
df_soilpar.loc[magway_mask, 7] = 0.8        #Ws = 0.8 (config 30n18)
df_soilpar.loc[magway_mask, 18] = 1         #DEPTH_1 = 1 (config 30n18)
df_soilpar.loc[magway_mask, 19] = 2         #DEPTH_2 = 2 (config 30n18)

# pyay
# df_soilpar.loc[pyay_mask, 4] = 0.6          #INFILT = 0.6 (config 30n18)
# df_soilpar.loc[pyay_mask, 5] = 0.9          #Ds = 0.9 (config 30n18)
# df_soilpar.loc[pyay_mask, 6] = 2            #Ds_MAX = 2 (config 30n18)
# df_soilpar.loc[pyay_mask, 7] = 0.8          #Ws = 0.8 (config 30n18)
# df_soilpar.loc[pyay_mask, 18] = 0.8         #DEPTH_1 = 0.8 (config 30n18)
# df_soilpar.loc[pyay_mask, 19] = 2           #DEPTH_2 = 2 (config 30n18)


# Save the updated dataframe as a new Excel file.
df_soilpar.to_csv(output_file, sep='\t',index=False, header=True)

print("Updated file saved as:", output_file)
