import requests
import pandas as p
from datetime import date
API_KEY = "83FH71K25QHEI0HN"
URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=SBIN.BSE&outputsize=full&apikey={API_KEY}"
Data = requests.get(url=URL)
DataList = Data.json()
OpenPriceList = []
HighPriceList = []
LowPriceList = []
ClosePriceList = []
DateList = []
Sum = 0
for i in DataList["Time Series (Daily)"]:
    if (int(i[0:4])< int(date.today().year) and int(i[0:4])>= int(date.today().year)- 5):
        Sum += float(DataList["Time Series (Daily)"][i]["4. close"])
        ClosePriceList.append(DataList["Time Series (Daily)"][i]["4. close"])
        OpenPriceList.append(DataList["Time Series (Daily)"][i]["1. open"])
        HighPriceList.append(DataList["Time Series (Daily)"][i]["2. high"])
        LowPriceList.append(DataList["Time Series (Daily)"][i]["3. low"])
        DateList.append(i)
CSVData1 = {"Date" : DateList,
            "Close" : ClosePriceList}
CSVData2 = {"Date" : DateList,
            "Open" : OpenPriceList,
            "High" : HighPriceList,
            "Low" : LowPriceList,
            "Close" : ClosePriceList}
NewData1 = p.DataFrame(CSVData1)
NewData2 = p.DataFrame(CSVData2)
NewData1.to_csv("ClosePrice.csv")
NewData2.to_csv("Stockinfo.csv")
print(f"Maximum Close Price : {max(ClosePriceList)}")
print(f"Minimum Close Price : {min(ClosePriceList)}")
print(f"Average Close Price : {Sum/len(ClosePriceList)}")
