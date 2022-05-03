#importing libraries
import pandas as pd
import numpy as np
import json
import urllib.request
from urllib.error import URLError, HTTPError
from Functions import json_collect, data_sort_write
import os
from datetime import date

#read in dataframe of facility locations
facilities = pd.read_excel('facility_locations.xlsx', engine='openpyxl')

#delete any rows where there are no coordinates
facilities.dropna(subset = ['latitude', 'longitude'], inplace=True)
facilities.reset_index(inplace=True)

#creating report and json urls
json_url = 'https://ejscreen.epa.gov/mapper/ejscreenRESTbroker.aspx?namestr=&geometry={{"spatialReference":{{"wkid":4326}},"x":{},"y":{}}}&distance=3&unit=9035&areatype=&areaid=&f=pjson'
report_url = 'https://ejscreen.epa.gov/mapper/EJSCREEN_report.aspx?namestr=&geometry={{"spatialReference":{{"wkid":4326}},"x":{},"y":{}}}&distance=3&unit=9035&areatype=&areaid=&f=report'

json_links = []
report_links = []

for i in range(0,len(facilities['latitude'])):
	json_links.append(json_url.format(facilities['longitude'][i],facilities['latitude'][i]))
	report_links.append(report_url.format(facilities['longitude'][i],facilities['latitude'][i]))

facilities['json'] = json_links
facilities['report_link'] = report_links

#pulling data using json links
json_dfs = json_collect(facilities)

#sorting dataframes
data_sort_write(json_dfs)