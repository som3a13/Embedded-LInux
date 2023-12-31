import requests

response=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')  
if response.status_code == 200:
    data=response.json()
    print(data['bpi']['USD'])
#############################################
##Data after formating
{
   "time":{
      "updated":"Oct 5, 2023 22:07:00 UTC",
      "updatedISO":"2023-10-05T22:07:00+00:00",
      "updateduk":"Oct 5, 2023 at 23:07 BST"
   },
   "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
   "chartName":"Bitcoin",
   "bpi":{
      "USD":{
         "code":"USD",
         "symbol":"&#36;",
         "rate":"27,426.3773",
         "description":"United States Dollar",
         "rate_float":27426.3773
      },
      "GBP":{
         "code":"GBP",
         "symbol":"&pound;",
         "rate":"22,917.2614",
         "description":"British Pound Sterling",
         "rate_float":22917.2614
      },
      "EUR":{
         "code":"EUR",
         "symbol":"&euro;",
         "rate":"26,717.2957",
         "description":"Euro",
         "rate_float":26717.2957
      }
   }
}