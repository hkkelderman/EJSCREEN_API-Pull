# EJSCREEN_API-Pull

The purpose of this document is to give some background information on EJSCREEN data, explain the code, and lay out the directions and best practices when using the EJSCREEN API Pull.

## EJSCREEN Data
[EJSCREEN](https://www.epa.gov/ejscreen/what-ejscreen) is an environmental justice mapping and screening tool that combines environmental and demographic indicators. When downloading EJSCREEN data, users input a geographic area and EJSCREEN returns demographic and environmental data for that area.
Currently, for the purposes of this code, **all EJSCREEN variables** are returned for a **3-mile radius** around a given coordinate pair. The data returned from EJSCREEN cannot be used in aggregate because it does not control for areas where one might double count (i.e. if a community is within 3 miles of more than one facility in a particular download). For more information on the limitations of EJSCREEN data, see [EPA’s webpage](https://www.epa.gov/ejscreen/limitations-and-caveats-using-ejscreen) on the issue.

Links to other useful resources:
1. [EJSCREEN Home Page](https://www.epa.gov/ejscreen)
2. [EJSCREEN Technical Documentation](https://www.epa.gov/sites/default/files/2021-04/documents/ejscreen_technical_document.pdf)
3. [EJSCREEN Field Descriptions](https://ejscreen.epa.gov/mapper/ejsoefielddesc.html)

## Files in this repository
1.	API Pull.py – The script used to scrape EJSCREEN data using their API.
2.	Functions.py - Functions used in the `API Pull` script.
3.	facility_locations – This is an excel spreadsheet, which is referenced by the application and contains the following columns:
    1. facility – The name of the facility.
    2. id – Any ID that might be associated with the facility. Can be NPDES, FRS ID, permit ID, etc.
    3. latitude
    4. longitude
    
    You will need to change this file each time you want to run the application for a new set of facilities. Since this EJSCREEN download application is based on coordinates, as long as you have latitude and longitude values, the program will run, but you should have at least the ‘facility’ or ‘id’ columns filled out too, so that you can more easily assign the EJSCREEN data to the proper facility.


