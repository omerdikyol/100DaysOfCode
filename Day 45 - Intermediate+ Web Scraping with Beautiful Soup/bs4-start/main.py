from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
  contents = file.read()
  
  
soup = BeautifulSoup(contents, "html.parser")
#print(soup.title)
#print(soup.title.name)                         # Name of title Tag
#print(soup.title.string)                       # Title's String

#print(soup.prettify())                         # All HTML file

#print(soup.a) # Returns first anchor tag

all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)

#for tag in all_anchor_tags:
  #print(tag.getText())                         # Returns all texts 
  #print(tag.get("href"))                       # Returns all links


heading = soup.find(name="h1", id="name")       # Returns particular one element
#print(heading)

section_heading = soup.find(name="h3", class_="heading")
#print(section_heading.text)

company_url = soup.select_one(selector="p a")   # Gives first selected item // Inside paranthesis = CSS Selector
#print(company_url)

my_name = soup.select_one(selector="#name")
#print(my_name)

headings = soup.select(".heading")
#print(headings)