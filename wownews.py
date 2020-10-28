# Imports shmimports
import bs4
import requests
from bs4 import BeautifulSoup
from re import search

# WoW news URL
news_url = 'https://news.blizzard.com/en-us/world-of-warcraft'

response = requests.get(news_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Search for articles
articles = soup.find_all('a', {"class": "ArticleLink"})

# Print all found articles
for article in articles:
	print("Title: ", article.get_text())
	print("Blog Post: ", article.get('data-article-id'))
	print("Link: ", article.get('href'))
	print()

# or

# Print only articles that have "patch" or "hotfixes"
hotfix = "(H|h)otfix"
patch = "(P|p)atch"
for article in articles:
	title = article.get_text()
	if search(hotfix, title) or search(patch, title):
		print("Title: ", article.get_text())
		print("Blog Post: ", article.get('data-article-id'))
		print("Link: ", article.get('href'))
		print()
