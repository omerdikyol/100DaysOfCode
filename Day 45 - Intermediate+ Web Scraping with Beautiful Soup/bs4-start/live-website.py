from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")

# Finding for the first article
""" article_tag = soup.find(name="a", class_="titlelink")
article_text = article_tag.getText()

article_link = article_tag.get("href")

article_upvote = soup.find(name="span", class_="score").getText()

print(article_text)
print(article_link)
print(article_upvote) """

# Finding for all articles

article_texts = []
article_links = []

articles = soup.find_all(name="a", class_="titlelink")

for article_tag in articles:
  text = article_tag.getText()
  article_texts.append(text)
  
  link = article_tag.get("href")
  article_links.append(link)
  
article_upvotes = [int(score.getText().split(' ')[0]) for score in soup.find_all(name="span", class_="score")]

#print(article_texts)
#print(article_links)
#print(article_upvotes)

largest_upvote = max(article_upvotes)
largest_upvote_index = article_upvotes.index(largest_upvote)

print(largest_upvote)
print(largest_upvote_index)
print(article_texts[largest_upvote_index+1])
print(article_links[largest_upvote_index+1])