from urllib import request
import os
import time

def stockchart(symb, startmonth, startday, startyear, endday, endmonth, endyear):

    charturl = "http://chart.finance.yahoo.com/table.csv?s=" + str(symb) + "&a=" + \
                                                               str(startmonth) + "&b=" + \
                                                               str(startday) + "&c=" + \
                                                               str(startyear) + "&d=" + \
                                                               str(endday) + "&e=" + \
                                                               str(endmonth) + "&f=" + \
                                                               str(endyear) + "&g=d&ignore=.csv"
    print ("Retrieving chart from: " + charturl)

    # Retrieve the webpage as a string
    response = request.urlopen(charturl)
    csv = response.read()

    # Save the string to a file
    csvstr = str(csv).strip("b'")

    lines = csvstr.split("\\n")
    savename = symb
    SaveDirectory = './stock_yahoo_data/'
    saveas = os.path.join(SaveDirectory,symb + str(time.time()) + '.csv')
    f = open(saveas, "w")
    for line in lines:
        f.write(line + "\n")
    f.close()
    time.sleep(1)
    return lines

'''
symb = input("Symbol: ")
startmonth = input("Starting Month: ")
startday = input("Starting Day: ")
startyear = input("Starting Year: ")
endday = input("Ending Day: ")
endmonth = input("Ending Month: ")
endyear = input("Ending Year: ")
'''
#symb = input("Symbol: ")
startmonth = 0
startday = 1
startyear = 2010
endday = 11
endmonth = 7
endyear = 2016

while True:
    symb = input("Symbol: ")
    stockchart(symb, startmonth, startday, startyear, endday, endmonth, endyear)
    print ("Saved.")