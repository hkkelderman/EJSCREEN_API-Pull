#importing libraries
import pandas as pd
import numpy as np
import json
import urllib.request
from urllib.error import URLError, HTTPError
import os
from datetime import date

def json_collect(df):
    """Takes a dataframe of facilities with formatted EJSCREEN JSON links and returns a dataframe
    of facilities with all EJSCREEN variables and an EJSCREEN report link.
    Both the EJSCREEN variables and report are for a 3-mile radius."""
    
    dfs = []
    
    for i in range(0,len(df['latitude'])):
        #grabs json data from url
        url = df['json'][i]
        try:
            response = urllib.request.urlopen(url)
        
        except URLError:
            print("{} didn't work.".format(df['facility'][i]))
        
        else:
            data = json.loads(response.read())
        
        #converting json data to dataframe and formatting
            temp = pd.DataFrame.from_dict([data])
            temp.reset_index(inplace=True)
        
        #adding facility information to new dataframe
            temp['facility'] = df['facility'][i]
            temp['id'] = df['id'][i]
            temp['latitude'] = df['latitude'][i]
            temp['longitude'] = df['longitude'][i]
            temp['report_link'] = df['report_link'][i]
        
            dfs.append(temp)
        
    return dfs

def data_sort_write(dfs):
    """Takes a list of dataframes that now have the EJSCREEN data for every coordinate pair, and then
    combines them into two separate dataframes, one for facilities with EJ data, and the other for
    facilities without EJ data."""

    day = date.today().strftime("%b-%d-%Y")
    dest = os.path.abspath(os.getcwd()) + '\\EJSCREEN Pull_{}'.format(day)
    os.mkdir(dest)

    data_dfs = []
    no_data_dfs = []

    for df in dfs:
        if len(df.columns) == 199: #if there is EJ data, there will be 199 columns
            data_dfs.append(df)
        else:
            no_data_dfs.append(df)

    if data_dfs:
        data_combined = pd.concat(data_dfs)
        data_combined.drop(columns = ['geometry', 'index'], inplace=True)
        d_cols = list(data_combined.columns)
        d_cols = d_cols[192:197] + d_cols[0:192]
        final_data = data_combined[d_cols]
        final_data.to_excel('{}\\Sites with EJSCREEN Data.xlsx'.format(dest), index=False)
    else:
        print('No facilities have EJ data.')
    
    if no_data_dfs:
        no_data_combined = pd.concat(no_data_dfs)
        final_no_data = no_data_combined.drop(columns = ['index'])
        final_no_data.to_excel('{}\\Sites without EJSCREEN Data.xlsx'.format(dest), index=False)
    else:
        print('All facilities have EJ data.')