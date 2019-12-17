import pandas
import requests
import json
import urllib3
from api_keys import cb_api_key

# construct URI
baseAPI = "https://api.census.gov/data/timeseries/poverty/saipe?"
categories = "&get=category_code,cell_value,data_type_code,error_data,geo_level_code,program_code,seasonally_adj,time_slot_id,time_slot_name"
timeseries = "&time=from+2001+to+2025"

# documentation for available variables located @ https://api.census.gov/data/timeseries/poverty/saipe/variables.html

params = {
    "COUNTY",
    "for",
    "GEOCAT",
    "GEOID" "in",
    "NAME",
    "SAEMHI_LB90",
    "SAEMHI_MOE",
    "SAEMHI_PT",
    "SAEMHI_UB90",
    "STABREV",
    "STATE",
    "YEAR",
}

# final URI
url = baseAPI + cb_api_key + params

# call the API and collect the response
response = requests.get(url)

# load the response into a JSON, ignoring the first element which is just field labels
responses = json.loads(response.text)

# store the response in a dataframe (below is an example)
new_home_construction = pandas.DataFrame(data=responses)
new_home_construction.columns = new_home_construction.iloc[0]
new_home_construction = new_home_construction[1:]

new_home_construction = new_home_construction.rename(
    columns={
        "category_code": "Category Code",
        "cell_value": "Cell Value",
        "data_type_code": "Data Type Code",
        "error_data": "Error Data",
        "geo_level_code": "Geo Level Code",
        "program_code": "Program Code",
        "seasonally_adj": "Seasonally Adjusted",
        "time_slot_id": "Time Slot ID",
        "time_slot_name": "Time Slot Name",
        "time": "Time",
    }
)

# save that dataframe to a CSV spreadsheet
new_home_construction.to_csv("new_home_construction.csv", index=False)

print("done")
