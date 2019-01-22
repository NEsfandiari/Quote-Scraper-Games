from bs4 import BeautifulSoup
import csv
import requests
import random
from time import sleep

quotes = []
authors = []
links = []
res = requests.get('http://quotes.toscrape.com')
soup = BeautifulSoup(res.text, 'html.parser')
while True:
    quotes.extend([quote.get_text() for quote in soup.select(".text")])
    authors.extend([author.get_text() for author in soup.select(".author")])
    links.extend([
        link.next_sibling.next_sibling['href']
        for link in soup.select(".author")
    ])
    btn = soup.find(class_='next')
    if btn:
        btn = btn.find('a')['href']
        res = requests.get(f'http://quotes.toscrape.com{btn}')
        soup = BeautifulSoup(res.text, 'html.parser')
        sleep(2)
    else:
        break

guesses = 4
rand = random.randint(0, len(quotes) - 1)
res2 = requests.get(f'http://quotes.toscrape.com{links[rand]}')
soup2 = BeautifulSoup(res2.text, 'html.parser')

while guesses > 0:
    guess = input(f"Who said this quote {quotes[rand]} ")
    if guess == authors[rand]:
        print("You Won")
        play = input("Play Again? Y/N ")
        if play == "Y":
            guesses = 4
            rand = random.randint(0, len(quotes) - 1)
            res2 = requests.get(f'http://quotes.toscrape.com{links[rand]}')
            soup2 = BeautifulSoup(res2.text, 'html.parser')
        else:
            break
    else:
        guesses -= 1
        if guesses == 3:
            print(
                f"Hint Birthdate and Location: {soup2.select('.author-born-date')[0].get_text()} {soup2.select('.author-born-location')[0].get_text()}"
            )
        elif guesses == 2:
            print(f"Hint First Name Letter: {authors[rand][0]}")
        elif guesses == 0:
            print("You LOSE!!!!")
