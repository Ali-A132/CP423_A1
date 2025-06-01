# Question 1: Web Scraping, Link Exploration, and Data Processing 
# [80 points]
# Your task involves creating a small search engine by scraping and 
# indexing the content from the historical population data of 
# Canadian provinces page on Wikipedia:

import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org"
visitedLinks = set()
idCounter = {"val": 1}

def getSoupFromLink(link):
    retrieve = requests.get(link, auth=('user', 'pass'))
    soup = BeautifulSoup(retrieve.text, 'html.parser')
    return soup

def excludeSections(soup):
    for s in soup.select('header, footer, nav, reflist, references, navbox, mw-heading3'):
        s.decompose()

    headings = ['h1', 'h2', 'h3']
    exclude = ["See also", "References", "Bibliography", "Further reading"]

    for heading in soup.find_all(headings):
        if heading.text in exclude:
            for text in heading.find_all_next():
                text.decompose()
            heading.decompose()
    return soup

def extractLinksFromPage(soup, limit = 5):
    linksList = []
    for link in soup.find_all('a'):
        linkVal = link['href']
        if '#' not in linkVal and ':' not in linkVal:
            jointURL = URL + linkVal
            if jointURL not in visitedLinks:
                linksList.append(jointURL)
            if len(linksList) >= limit:
                break
    return linksList

def extractHyperlinks(link, depth, maxDepth, folder):
    if link in visitedLinks or depth > maxDepth:
        return

    visitedLinks.add(link)
    soup = getSoupFromLink(link)
    soup = excludeSections(soup)

    element = soup.find('div', class_='mw-page-container')
    text = element.get_text(separator='\n', strip=True)

    title = link.split("/wiki/")[-1]
    fileId = idCounter["val"]
    filename = f"{folder}/depth{depth}_id_{fileId}_{title}.txt"
    idCounter["val"] += 1

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

    if depth < maxDepth:
        childLinks = extractLinksFromPage(soup)
        for child in childLinks:
            extractHyperlinks(child, depth + 1, maxDepth, folder)

folder = "scrappedInfo"
os.makedirs(folder, exist_ok=True)

startLink = "https://en.wikipedia.org/wiki/List_of_Canadian_provinces_and_territories_by_historical_population"
extractHyperlinks(startLink, depth = 1, maxDepth = 3, folder = folder)
