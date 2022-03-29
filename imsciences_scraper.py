#The following code scrapes the latest news from https://imsciences.edu.pk

#importing the required modules
import requests
from bs4 import BeautifulSoup

#downloading the page to be scraped
url = "https://imsciences.edu.pk/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


#narrowing down and getting the information required
table_div = soup.find("div", class_="col-sm-7")
table_rows = table_div.find_all("tr")

#printing the extracted information to the console
for row in table_rows: 
    print(row.strong.get_text().strip())
    print(row.b.get_text().strip())
    print(str(row.a["href"]))
    print()
    
#todo: some links in the output contains spaces. those links need to be manually pasted in the browser to work. deal with it.
    

