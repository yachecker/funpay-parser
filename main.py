from bs4 import BeautifulSoup
import requests

# initialize
url = 'https://funpay.com/lots/83/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
rusChars = 'йцукенгшщзфывапролдячсмитьбюёЙЦУКЕНГШЩЗФЫВАПРОЛДЯЧСМИТЬБЮЁ'
users = []
reviews = []

# collect data
allUsers = soup.findAll('a', class_='tc-item')
allReviews = soup.find_all('div', class_='media-user-reviews')

# remove russian chars


def removeTheShit(a):
    return int(a.strip(rusChars))


# url collecting process
for b in allUsers:
    users.append(b['href'])

# reviews collecting process
for a in allReviews:
    if a.text == 'нет отзывов':
        reviews.append(0)
    else:
        reviews.append(removeTheShit(a.text.strip('\n')))

# creating file
file = open('OhYEAAH.txt', 'w')
file.write(f'===========PARSED {len(users)} USERS===========\n')

# printing results
print(f'Пользователей: {len(users)}, Отзывов: {len(reviews)}')

# recording results in file
for a in range(len(users)):
    file.write(f'{users[a]} - {reviews[a]}\n')
file.close()
