import requests
from datetime import datetime
from pytz import reference
import sys

data={
    "Date":"",
    "Name":"",
    "Price":"",
    "Value Change":"",
    "Percent Change":"",
}
def getInfo(name):

    SYMBOL_URL="https://www.alphavantage.co/query?function=OVERVIEW&symbol="+name+"&apikey="+"E1NGKWLLXPZE46U4"
    DETAILS_URL="https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="+name+"&apikey="+"E1NGKWLLXPZE46U4"
    response={}
    try:
        
        response = requests.get(SYMBOL_URL).json()
        
        print("hell")
        localtime = reference.LocalTimezone()
        data["Date"]=datetime.now().strftime("%a, %b %d %H:%M:%S, " + localtime.tzname(datetime.now())+" %Y")
        data["Name"]=response["Name"]+"("+ response["Symbol"]+")"
        response = requests.get(DETAILS_URL).json()

        print(response)
        data["Price"]=response["Global Quote"]["05. price"]
        change=float(response["Global Quote"]["09. change"])
       # data["valueChange"]="+"+str(change) if change>0 else "-"+str(change)
        percentChange=response["Global Quote"]["10. change percent"]
       # data["percentChange"]=percentChange if float(percentChange[0:len(percentChange)-1])>0 else percentChange
        data["Value Change"]= "+"+str(change) if change>0 else change
        data["Percent Change"]="+"+percentChange if float(percentChange[0:len(percentChange)-1])>0 else percentChange
        return data

    except :
        print(sys.exc_info()[0])
        if(len(response) == 0):
            return "Please enter a valid symbol"
        else:
            return "Network error, please try again after sometime"


    