import urllib.request
import os

def download():
    urls = (
        'https://www.statista.com/statistics/275555/median-age-of-the-population-in-mexico/',
        'https://www.statista.com/statistics/275391/median-age-of-the-population-in-france/',
        'https://www.statista.com/statistics/254361/average-age-of-the-population-in-brazil/',
        'https://www.statista.com/statistics/241494/median-age-of-the-us-population/',
        'https://www.statista.com/statistics/624303/average-age-of-the-population-in-germany/',
        'https://www.statista.com/statistics/261339/life-expectancy-at-birth-in-switzerland/',
        'https://www.statista.com/statistics/408007/average-age-of-the-population-in-algeria/',
        'https://www.statista.com/statistics/524614/average-age-of-the-population-in-tunisia/',
        'https://www.statista.com/statistics/326829/average-age-of-the-population-in-iraq/',
        'https://www.statista.com/statistics/326576/average-age-of-the-population-in-syria/',
        'https://www.statista.com/statistics/382229/average-age-of-the-population-in-nigeria/',
        'https://www.statista.com/statistics/255480/median-age-of-the-population-in-turkey/',
        'https://fr.statista.com/statistiques/785233/age-median-de-la-population-iran/',
        'https://www.statista.com/statistics/368964/average-age-of-the-population-in-colombia/',
        'https://www.statista.com/statistics/370768/average-age-of-the-population-in-venezuela/',
        )

    for url in urls:
      segments = [field for field in url.split('/') if field]
      name = segments[-1].split('-')[-1]
      response = urllib.request.urlopen(url)
      data = response.read()
      with open(name + 'html', 'wb') as output:
          output.write(data)

def parse(filename):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(open(filename), "html.parser")
    table = soup.find("table", {"id": "statTable"})
    
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    data = list()
    country = filename.split('.')[0]
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append((country, cols[0], cols[1]))
    
    return data

def run():
    data = list()
    for filename in os.listdir():
        if not filename.endswith('.html'):
            continue
        
        data += parse(filename)
    
    for row in data:
        print(','.join(row))

run()