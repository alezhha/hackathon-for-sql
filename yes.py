import requests
import psycopg2
from bs4 import BeautifulSoup

connectionHtml = requests.get('http://kinoteatr.kg/index.php/category/view?id=1')

soup = BeautifulSoup(connectionHtml.text, "html.parser")

names = []
genres = []
years = []

titles = soup.find_all(class_="card-title text-danger")

for i in titles:
    names.append(i.text)


prikol = soup.find_all(class_="card-text")
for i in prikol:
    if 'Год:' in i.text:
        x = str(i.text).split(': ')
        years.append(int(x[1]))
    elif 'Жанр:' in i.text:
        x = str(i.text).split(':  ')
        if '\r\n' not in i.text:
            genres.append(x[1])
        else:
            x = x[1].split('\r\n')
            genres.append(x[1])

connectionSql = psycopg2.connect(
    database = 'alezhhahp',
    user = 'postgres', 
    password = 'zxcv1234',
    host = 'localhost',
    port = '5432' 
)

query = """
    INSERT INTO list_of_films (name, release_year, genre) VALUES 
"""

for i in range(len(names)):
    query+=f"""('{names[i-1]}',
    {years[i-1]},
    '{genres[i-1]}'),"""

sql_query = query[:-1]+';'

cursorSql = connectionSql.cursor()

cursorSql.execute(sql_query)

connectionSql.commit()
cursorSql.close()
connectionSql.close()
