import requests
import pandas as pd

Countys = ['Bristol County, Rhode Island', 'Kent County, Rhode Island', 'Newport Conty, Rhode Island', 'Providence Island, Rhode Island', 'Washington County, Rhode Island']
Population = []
Median_age = []
Companies = []
Place_name_ = []


def main():
    for County in Countys:
        Place_name_.append(requests.get("https://factfinder.census.gov/rest/communityFactsNav/nav?", params = {'searchTerm': County, 'spotlightId': 'ALL'}).json()['CFMetaData']['geo'])
        Population.append(requests.get('https://factfinder.census.gov/rest/communityFactsNav/nav?', params= {'searchTerm': County, 'spotlightId':'ALL'}).json()['CFMetaData']['measuresAndLinks']['allMeasures'][0]['list'][1]['value'])
        Median_age.append(requests.get('https://factfinder.census.gov/rest/communityFactsNav/nav?', params={'searchTerm': County, 'spotlightId': 'ALL'}).json()['CFMetaData']['measuresAndLinks']['allMeasures'][1]['value'])
        Companies.append(requests.get('https://factfinder.census.gov/rest/communityFactsNav/nav?', params={'searchTerm': County, 'spotlightId': 'ALL'}).json()['CFMetaData']['measuresAndLinks']['allMeasures'][2]['value'])

    data = pd.DataFrame({
        'Place_name ': Place_name_,
        'Population ': Population,
        'Age ': Median_age,
        'Business ': Companies

    })



    print(data)
    data.to_csv('data_of_RhIsl.csv')


if __name__ == '__main__':
    main()
