import requests
import simplejson as json
import pandas as pd

APIKEY = "AIzaSyClgt6mOSkM_OFIGmYlAyvnS8gUWlA4H8Y"
Place_id = []
Name = []
Opening_hours = []
Website = []
Name2 = []
Phone = []
Address = []
Rating = []



def findPlaces(pagetoken = None):
   query = "law+firms+massachusetts"
   url = "https://maps.googleapis.com/maps/api/place/textsearch/json?&query={query}&key={APIKEY}{pagetoken}".format(query = query,APIKEY = APIKEY, pagetoken = "&pagetoken="+pagetoken if pagetoken else "")
   print(url)
   response = requests.get(url)
   res = json.loads(response.text)
   print(type(res))
   print("here results ---->>> ", len(res["results"]))

   for result in res["results"]:
      info = ";".join(map(str,[result["name"]]))
      info2= ";".join(map(str,[result["place_id"]]))

      Place_id.append(info2)

   pagetoken = res.get("next_page_token",None)

   print("here -->> ", pagetoken)

   return pagetoken


pagetoken = None

while True:
     pagetoken = findPlaces(pagetoken=pagetoken)
     import time
     time.sleep(5)

     if not pagetoken:
         break







for plc in Place_id:
    APIKEY2 = 'AIzaSyClgt6mOSkM_OFIGmYlAyvnS8gUWlA4H8Y'
    fields = 'name,formatted_address,international_phone_number,rating,opening_hours/weekday_text,website'
    url2 = "https://maps.googleapis.com/maps/api/place/details/json?&place_id={place_id}&fields={fields}&key={APIKEY}".format(place_id = plc,fields= fields,APIKEY = APIKEY2)
    r2=requests.get(url2)
    res = json.loads(r2.text)

    results2 = res.get('result')
    # open_hours = results2.get('opening_hours')

    Phone.append(results2.get('international_phone_number'))
    Address.append(results2.get('formatted_address'))
    # Opening_hours.append(open_hours.get('weekday_text'))
    Website.append(results2.get('website'))
    Rating.append(results2.get('rating'))
    Name2.append(results2.get('name'))

    print(url2)












data = pd.DataFrame({
        'Name': Name2,
        'Address':Address,
        'Phone': Phone,
        'Website': Website,
        # 'Opening hours': Opening_hours,
        'Rating': Rating



    })


data.to_csv('data_o1.csv')


