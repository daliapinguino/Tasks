import requests
import simplejson as json
import pandas as pd

APIKEY = "AIzaSyBmODL4WJ5xSxzM5eB6rhe36FECN-k6ydQ"
Place_id = [
'ChIJt42q74Rw44kRI5iyxHJgwZU',
'ChIJWVDs7oRw44kR_WSLrAzvkKM',
'ChIJH_wRsYNw44kR4kaqjhk6W0E',
'ChIJDdmKQoJw44kRsThkdjV-Ob0',
'ChIJdz88sIRw44kR-qJXJ5ho7yw',
'ChIJJ2f7GoRw44kRwEMwaqQjH2Q',
'ChIJS9iwtIVw44kRSFk9vcmUTq8',
'ChIJkXYkfAx644kR_IroKLbIshI',
'ChIJ2x1UlINw44kR-MKsyIuhFLE',
'ChIJ6YSTIoZw44kRhEKBULs8w_U',
'ChIJs-osUYNw44kRGo6fqyiBNPM',
'ChIJ0VvNp3hw44kR7815Q9dWGYY',
'ChIJeSliTZtw44kRNBTwFrwLXio',
'ChIJz88Sd1R344kR8rICmRbh9ZI',
'ChIJM34IdoRw44kR-LM5xRx_T5g',
'ChIJDVKqXoRw44kRymz059u3R1s',
'ChIJfXD4ZlF344kRNmzUE7TTPI8',
'ChIJU9XyRIZw44kRgnV2Aqv6luM',
'ChIJEbKSrYRw44kRTt8Z0_o3eWs',
'ChIJb0mRGoRw44kR6b-40QF1Nbc',
'ChIJ9d2bt49w44kRyguxZMb5aIM',
'ChIJb7nX2YVw44kRDAMoO_ZJM-8',
'ChIJSQsjYIRw44kRuUBwhj_s3p8',
'ChIJw7I2SVF344kRBSF0EGGXWuQ',
'ChIJeSliTZtw44kRd4K-KBBdjSg',
'ChIJD75e1YBw44kRPSkGw-oYYUY',
'ChIJD75e1YBw44kRPSkGw-oYYUY',
'ChIJIVrPZnR644kRKRNQm331JWA',
'ChIJIVrPZnR644kRKRNQm331JWA',
'ChIJIVrPZnR644kRKRNQm331JWA',
'ChIJIVrPZnR644kRKRNQm331JWA',
'ChIJ8WpGfIZw44kRUQsLVSEn3go',
'ChIJAzQhjVB344kRKkAH4672GAU',
'ChIJAzQhjVB344kRKkAH4672GAU',
'ChIJE4xuJhW44IkRzSsM2o53oJo',
'ChIJ_58pzYxw44kRnL3DZDj1htg',
'ChIJNdmJ34Rw44kRMPR8a-LoXK4',
'ChIJj9eBzwp644kRH6KEjICJ3sM',
'ChIJgwJuygJ644kRd1W6R0QwpzI',
'ChIJR47FR4Jw44kR83_0sGtmO7M',
'ChIJs5XhIAx644kR8DdWoRmYb7Y',
'ChIJz4WiIYRw44kRzIzeTJ0ZV68',
'ChIJ-Z6bio5w44kRD0YxReMcaac',
'ChIJy4euoJp644kRVAXeUNrI8O8',
'ChIJy4euoJp644kRVAXeUNrI8O8',
'ChIJy4euoJp644kRVAXeUNrI8O8',
'ChIJ_S8xi3R644kRPe8Ga_v4Ct4',
'ChIJV1vqPMWd44kR8q_2l0DBeJM',
'ChIJV1vqPMWd44kR8q_2l0DBeJM',
'ChIJV1vqPMWd44kR8q_2l0DBeJM',
'ChIJDdmKQoJw44kRUc_dAwI1dj0',
'ChIJ-WO8LGUU44kRZAG75XfzhU8',
'ChIJ-WO8LGUU44kRZAG75XfzhU8',
'ChIJu3ImvqVw44kRPIJmlSfBvWA',
'ChIJu3ImvqVw44kRPIJmlSfBvWA',
'ChIJNRzsAodw44kRgWQCXswP0OU',
'ChIJR47FR4Jw44kRfNSUvhJc-rM',
'ChIJR47FR4Jw44kRfNSUvhJc-rM',
'ChIJ8yBRDWQG5IkRUMzgzFw4KQ0',
'ChIJYVdYIoJw44kRhJrEmGDeu7s',
'ChIJBwKl1x9644kRB1keGFAGeBE',
'ChIJ89Bs3FZ244kRypONCLkxG0o',
'ChIJGdcWKBxdXEARVu6Gh253xa8',
'ChIJH_wRsYNw44kRBC7XiwzQxN4',
'ChIJH_wRsYNw44kRBC7XiwzQxN4',
'ChIJR47FR4Jw44kRH5r5QaeVCM4',
'ChIJN7wZYIRw44kRLqsfWfOVdj4',
'ChIJlW3SKT-k44kRCuJy2DSaxeE',
'ChIJlW3SKT-k44kRCuJy2DSaxeE',
'ChIJkUMThoZw44kRwbHs2nNtAJk',
'ChIJ-dc4e4Zw44kRNMyo7GozfgQ',
'ChIJDdmKQoJw44kR0Swh7gtjf2A',
'ChIJpaacq6OK44kRyUytujaVKIw',
'ChIJpaacq6OK44kRyUytujaVKIw',
'ChIJvwqYLYRw44kRwfi8qrOeuPo',
'ChIJkRwmJW1644kRm5oOV2YzvC8',
'ChIJkRwmJW1644kRm5oOV2YzvC8',
'ChIJdz88sIRw44kRzj_8WvUr0YQ',
'ChIJdz88sIRw44kRzj_8WvUr0YQ',
'ChIJbaxH2WQU44kRcaaA2tYBxrw',
'ChIJI0Tv839644kR3CEP5III6xg',
'ChIJq6qq5qIW44kRqkPDxKm6f6E',
'ChIJb7nX2YVw44kRMbVq0pKXpfY',
'ChIJ9VkyssoM44kRNBKruYNKOJE',
'ChIJa04qjoRw44kRrKROYfSqhYQ',
'ChIJa04qjoRw44kRrKROYfSqhYQ',
'ChIJPV8P0oVw44kRYdPxfbb0Kx8',
'ChIJPV8P0oVw44kRYdPxfbb0Kx8',
'ChIJB6ew5s-d44kREDKoYcVEp84',
'ChIJ6w1FtmYG5IkRMi1_tLJd6Xg',
'ChIJ6w1FtmYG5IkRMi1_tLJd6Xg',
'ChIJbXJX4qqM5IkRPjIMOuxQQ4c',
'ChIJbXJX4qqM5IkRPjIMOuxQQ4c',
'ChIJbXJX4qqM5IkRPjIMOuxQQ4c',
'ChIJbXJX4qqM5IkRPjIMOuxQQ4c',
'ChIJ5U_bC8GD44kRGkoRO-M2RTg',
'ChIJ5U_bC8GD44kRGkoRO-M2RTg',
'ChIJ-dSc1-Pm5okRaPN99oCOW-4',
'ChIJ-dSc1-Pm5okRaPN99oCOW-4',
'ChIJ-dSc1-Pm5okRaPN99oCOW-4',
'ChIJXfaDLoJw44kRpmxqACxYvos',
'ChIJq4g0sKeC44kRMa1IW_M5_00',
'ChIJGy1WT4B744kRTKPyTAy28EY',
'ChIJ_8zKJ9hx44kR-poZSab3xw4',
'ChIJm3aSM3R644kRiJ3VmzP3Afk',
'ChIJZxwzz4Nw44kRou8iOm3P95c',
'ChIJZxwzz4Nw44kRou8iOm3P95c',
'ChIJZxwzz4Nw44kRou8iOm3P95c',
'ChIJPaVhZYJw44kRGgSC9V0Mc_I',
'ChIJexX1pxh944kR9MTLoouVZl4',
'ChIJ7X_-xBF644kR1ZPMHpufIVk',
'ChIJ7X_-xBF644kR1ZPMHpufIVk',
'ChIJ7X_-xBF644kR1ZPMHpufIVk',
'ChIJCVRq85Bw44kRN_d1Iyihhtk',
'ChIJ9dhKUSWD44kRDh23CMMtMs0',
'ChIJ9dhKUSWD44kRDh23CMMtMs0',
'ChIJ9dhKUSWD44kRDh23CMMtMs0',
'ChIJPRSasoRw44kR06oiwnNPjB0',
'ChIJPRSasoRw44kR06oiwnNPjB0',
'ChIJPRSasoRw44kR06oiwnNPjB0',
'ChIJk8TlRoJw44kRkN-Ms2k6K5g',
'ChIJyQ-O0YBw44kRyjL3ad8mdx4',
'ChIJWbK0ghSk44kReziJQEfaoac',
'ChIJUQXt-YZw44kRdepjUQU0igo',
'ChIJUQXt-YZw44kRdepjUQU0igo',
'ChIJs-osUYNw44kRaI_Z31fqRH8',
'ChIJcUjuhVeI44kRWObmvId62BY',
'ChIJUyfCio5w44kRcW_KZHnbq_0',
'ChIJ02pGfIZw44kR2ixNa5H2IHg',
'ChIJ02pGfIZw44kR2ixNa5H2IHg',
'ChIJ02pGfIZw44kR2ixNa5H2IHg',
'ChIJ0TLzuIZw44kRsn2MOTektaE',
'ChIJ0TLzuIZw44kRsn2MOTektaE',
'ChIJ0TLzuIZw44kRsn2MOTektaE',
'ChIJV-uoJcWd44kR2ODZ_BW5M-Y',
'ChIJv7UHwwt644kRmokLMHvInWM',
'ChIJzxdZj4Nw44kRiGOCoEL4Vsg',
'ChIJA_c0BIJw44kRVsivVtZN7xE',
'ChIJXcQ5xYNw44kR11VvIvWS5ho',
'ChIJXcQ5xYNw44kR11VvIvWS5ho',
'ChIJL9r0lGcG5IkRy-sxuL7odyc',
'ChIJ-xSOdW5544kR-Qwjsdh99Ms',
'ChIJe2KniSaK44kRbMKC4r1M8SY',
'ChIJa5tN6YFw44kR3vJUA5qY0iw',
'ChIJ5aEk7Qx644kR6Id5CSq1o_Y',
'ChIJMRfeHYRw44kRkj0O9BFa16I',
'ChIJMRfeHYRw44kRkj0O9BFa16I',
'ChIJMRfeHYRw44kRkj0O9BFa16I',
'ChIJMRfeHYRw44kRkj0O9BFa16I',
'ChIJMRfeHYRw44kRkj0O9BFa16I',
'ChIJz99buIZw44kR7WVCsimKBZg',
'ChIJz99buIZw44kR7WVCsimKBZg',
'ChIJz99buIZw44kR7WVCsimKBZg',
'ChIJz99buIZw44kR7WVCsimKBZg',
'ChIJEZRW7I6e44kR9UJHJrLXbEI',
'ChIJhwlaZodw44kRJtIFFPKScjg',
'ChIJC3tMz4Nw44kRZyK00p2z-lk',
'ChIJjec1OQJi44kR5Lx2v3rjp4I',
'ChIJjec1OQJi44kR5Lx2v3rjp4I',
'ChIJjec1OQJi44kR5Lx2v3rjp4I',
'ChIJH9CZLYRw44kRmUk9Uicm-BI',
'ChIJD75e1YBw44kRBrVLZsSXlKw',
'ChIJSV_d839644kRLihPsqRN4og',
'ChIJSV_d839644kRLihPsqRN4og',
'ChIJSV_d839644kRLihPsqRN4og',
'ChIJSV_d839644kRLihPsqRN4og',
'ChIJgwJuygJ644kRc5nnXy_vhQY',
'ChIJZ6RitVCB44kRm6JQ8m0p6XA',
'ChIJPSB-djuX44kRxSH_FM4PJmA',
'ChIJb9wFS4Fw44kRCubMXRXgN-E',
'ChIJLWMRrgWZ44kRWWRN5yNBFRg',
'ChIJLWMRrgWZ44kRWWRN5yNBFRg',
'ChIJLWMRrgWZ44kRWWRN5yNBFRg',
'ChIJe5MyL4dw44kRvPsKHbfBN74',
'ChIJl2aJQ6WD44kRAKe1jPc8iB0',
'ChIJl2aJQ6WD44kRAKe1jPc8iB0',
'ChIJEX2BLF-T5IkRGqQnvh82Xco',
'ChIJ-4U7rebm5okRhQ52SfgH3T8',
'ChIJb-HKBWcG5IkRV4tpSBZGE2o',
'ChIJU2c1LePm5okRtUKvWI-OORw',
'ChIJKyl61dif44kR-dEUyCA8VcE',
'ChIJBToZB5p_44kRf5FUN_3_EGQ',
'ChIJnQvI54Rw44kRPLPR9dcQCNQ',
'ChIJafuXv_J344kRMf5_ANpCqlY',
'ChIJu5iqC7h244kRdVoCICh3oCo',
'ChIJHW3Eu7N144kRqlINXq7gcu8',
'ChIJrXO36IeB44kRd7i9HlYA_r0',
'ChIJrXO36IeB44kRd7i9HlYA_r0',
'ChIJn3VRo4Zw44kRODaAyslwc1k',
'ChIJTYeHlINw44kR4bB8yEgDFhs',
'ChIJTYeHlINw44kR4bB8yEgDFhs',
'ChIJXYs-K8-g44kRFwBNzQO5TXc',
'ChIJXYs-K8-g44kRFwBNzQO5TXc',
'ChIJXYs-K8-g44kRFwBNzQO5TXc',
'ChIJKQXNttad44kRc6_1LvD1nWE',
'ChIJnYV-aPSQ44kRzSV7ZFg9ZRc',
'ChIJnYV-aPSQ44kRzSV7ZFg9ZRc',
'ChIJnYV-aPSQ44kRzSV7ZFg9ZRc',
'ChIJf21yHzF044kRSL3mZEiwWkQ',
'ChIJcfUSoSX144kRTOT2pIY3PKE',
'ChIJsdF-7WFx44kRo7g90PltkS4',
'ChIJOdvhH2cG5IkR4KQaY_6NH8s',
'ChIJlU20X8Wd44kRkzf0f2Eo9_w',
'ChIJPfY20ouI44kRmiaxQ_4ShGA',
'ChIJPfY20ouI44kRmiaxQ_4ShGA',
'ChIJp-UCSsaD44kR0_RXaxJpbF4',
'ChIJp-UCSsaD44kR0_RXaxJpbF4',
'ChIJp-UCSsaD44kR0_RXaxJpbF4',
'ChIJJQniZ0KL44kRy-DUo_ZNtPY',
'ChIJJQniZ0KL44kRy-DUo_ZNtPY',
'ChIJhVjYlRuj44kRoMIINFj2Pvg',
'ChIJw-pnRaqb44kR1JpI6KGLP-8',
'ChIJP8A6Ys5544kRMHtbV7zS2G0',
'ChIJP8A6Ys5544kRMHtbV7zS2G0',
'ChIJDdmKQoJw44kRVTvZRumoCUg',
'ChIJ1WOPl4Nw44kR3Qn5IcU4YnM',
'ChIJ1WOPl4Nw44kR3Qn5IcU4YnM',
'ChIJ1WOPl4Nw44kR3Qn5IcU4YnM',
'ChIJG20lc9KM44kR0cC_vN72-mU',
'ChIJG20lc9KM44kR0cC_vN72-mU',
'ChIJSWnQhZ6F44kR8jeJGBU87qs',
'ChIJTbrQ0HN744kRQxjwHHdyAqg',
'ChIJ0VvNp3hw44kRABItU97vr2I',
'ChIJI4aCdc2Q44kRvRu5WI7zgz0',
'ChIJ77dfG4Rw44kRPhWFosjEiRA',
'ChIJ77dfG4Rw44kRPhWFosjEiRA',
'ChIJyW0YK51w44kRqRqzKSwlnig',
'ChIJlzIfIBR144kRUhNFzEQn0U4',
'ChIJkSvAY4mL44kRP2at80moZ9Q',
'ChIJ7xh5c6Rw44kRlze3uiYA3GU',
'ChIJ0VvNp3hw44kRnVOULbRnOtA',
'ChIJ0VvNp3hw44kRnVOULbRnOtA',
'ChIJw_exBH1x44kR6f36VH4LnmM',
'ChIJf9U9BROC44kR9O3WsceT62Q',
'ChIJ1WOPl4Nw44kRIJJ2EdA8vHE',
'ChIJU2hMAoRw44kR50utIQCGSIA',
'ChIJU2hMAoRw44kRfIZe1Tgm9jY',
'ChIJEYspG-S65IkRFNolGxA347k',
'ChIJU0psAINw44kRFqPS0O0tFHU',
'ChIJU0psAINw44kRFqPS0O0tFHU',
'ChIJ3y-8pJB_44kR1zqN0mCDen4',
'ChIJ5fYEfTCD44kRv-zUrVxqbc8',
'ChIJG_86BCmR44kRepTCD7O-dCw',
'ChIJB2ZkSXuk44kRL_FzKok9Ke0',
'ChIJM_YBnjCe44kR7UDDTgjRCNU',
'ChIJM_YBnjCe44kR7UDDTgjRCNU',
'ChIJD0iEuVR15IkRmc8xrquQC0I',
'ChIJ87w0-xuj44kRoG6DjSLADos',
'ChIJWWcEYKqJ44kRulr7kETJkw0',
'ChIJWWcEYKqJ44kRulr7kETJkw0',
'ChIJD75e1YBw44kRXqexr5bCzOg',
'ChIJD75e1YBw44kRXqexr5bCzOg',
'ChIJD75e1YBw44kRXqexr5bCzOg',
'ChIJD75e1YBw44kRXqexr5bCzOg',
'ChIJk-4vIJBw44kRqWqoDVZhInY',
'ChIJh6XMxhF644kRZJneRdwo5n4',
'ChIJlRjtSohw44kRemfJ5IiScLw',
'ChIJpd0QIRl944kRiqJzgrNksj8',
'ChIJpd0QIRl944kRiqJzgrNksj8',
'ChIJJRC3MYdw44kR6OxBrX1X6dU',
'ChIJdz88sIRw44kRmqknId6BkS0',
'ChIJF7uLcRAM44kRrL23iVl9U7g',
'ChIJsdISGDKe44kRf4cWy0HSyCo',
'ChIJbzwvN3ea44kRafPLl6HV4LY',
'ChIJPxvnNIhw44kR8HhsWXLxuTk',
'ChIJPaVhZYJw44kRod0xWuDLEm4',
'ChIJH9CZLYRw44kRSXQjGqHqDcc',
'ChIJJRC3MYdw44kRD7bGyoVgx4E',
'ChIJp7EeZOkw-4kRUrGIR2XpFmU',
'ChIJDVKqXoRw44kR7g5GfnYLnlE',
'ChIJNXY-fIJ644kR5HUdDWTXq74',
'ChIJa5tN6YFw44kRVbbFQDNvlik',
'ChIJDdmKQoJw44kRCv5grRMqR4A',
'ChIJPaVhZYJw44kRPjhxbxj0_mk',
'ChIJPfY20ouI44kR0sT-vvFmqQ4',
'ChIJzdGLZe1444kR5hnnIvtEDcE',
'ChIJuTIn94Jw44kRYfMY_igcdlQ',
'ChIJDZXmNJAK5IkRrjXAe0iFe6M',
'ChIJPaVhZYJw44kR1EFy0FRQ87E',
'ChIJNXY-fIJ644kRZHKfyuvtWRs',
]
Name = []
Opening_hours = []
Website = []
Name2 = []
Phone = []
Address = []
Rating = []



# def findPlaces(pagetoken = None):
#    query = "law+firms+massachusetts"
#    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?&query={query}&key={APIKEY}{pagetoken}".format(query = query,APIKEY = APIKEY, pagetoken = "&pagetoken="+pagetoken if pagetoken else "")
#    print(url)
#    response = requests.get(url)
#    res = json.loads(response.text)
#
#    print("Quantity of places ---->>> ", len(res["results"]))
#
#    for result in res["results"]:
#       info2= ";".join(map(str,[result["place_id"]]))
#
#       Place_id.append(info2)
#
#    pagetoken = res.get("next_page_token",None)
#
#    print("Pagetoken for the next page -->> ", pagetoken)
#
#    return pagetoken
#
#
# pagetoken = None
#
# while True:
#      pagetoken = findPlaces(pagetoken=pagetoken)
#      import time
#      time.sleep(5)
#
#      if not pagetoken:
#          break







for plc in Place_id:
    APIKEY2 = 'AIzaSyClgt6mOSkM_OFIGmYlAyvnS8gUWlA4H8Y'
    fields = 'name,formatted_address,international_phone_number,rating,opening_hours/weekday_text,website'
    url2 = "https://maps.googleapis.com/maps/api/place/details/json?&place_id={place_id}&fields={fields}&key={APIKEY}".format(place_id = plc,fields= fields,APIKEY = APIKEY2)
    r2=requests.get(url2)
    res = json.loads(r2.text)

    results2 = res.get('result')


    open_hours = results2.get('opening_hours')
    if open_hours is None:
        Opening_hours.append('None')
    else:
        Opening_hours.append(open_hours.get('weekday_text'))

    Phone.append(results2.get('international_phone_number'))
    Address.append(results2.get('formatted_address'))
    Website.append(results2.get('website'))
    Rating.append(results2.get('rating'))
    Name2.append(results2.get('name'))















data = pd.DataFrame({
        'Name': Name2,
        'Address':Address,
        'Phone': Phone,
        'Website': Website,
        'Opening hours': Opening_hours,
        'Rating': Rating



    })


data.to_csv('Law_firms.csv')


