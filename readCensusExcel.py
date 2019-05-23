#!python37

'''
This is what your program does:
•	 Reads the data from the Excel spreadsheet.
•	 Counts the number of census tracts in each county.
•	 Counts the total population of each county.
•	 Prints the results.
This means your code will need to do the following:
•	 Open and read the cells of an Excel document with the openpyxl module.
•	 Calculate all the tract and population data and store it in a data structure.
•	 Write the data structure to a text fle with the .py extension using the
pprint module.
'''
import openpyxl,pprint
print('Opening workbook...')
wb=openpyxl.load_workbook('censuspopdata.xlsx')
sheet= wb.get_sheet_by_name("Population by cesus tract")
countryData={}
#fill in the countrydata with each country's population and tract

for row in range(2,sheet.get_highest_row()+1):
    #each row in the spreadshhet has data for one census tract
    state=sheet['B'+str(row)].value
    country=sheet['C'+str(row)].value
    pop=sheet['D'+str(row)].value
    countryData.setdefault(state,{})
    countryData[state].setdefault(country,{'tracts': 0,'pop : 0'})
    countryData[state][countyr]['tracts']+=1
    countryData[state][country]['pop']+=int(pop)
    print('writing results...')
    resultFile=open('census2010.py','w')
    resultFile.write('allData= '+pprint.format(countryData))
    resultFile.close()
    print('Done')

