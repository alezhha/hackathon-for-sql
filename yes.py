import requests
import psycopg2
import BeautifulSoup

connectionHtml = requests.get('https://www.kinopoisk.ru/lists/editorial/theme_school/')

soup = BeautifulSoup(resp.text, "html.parser")


connectionSql = psycopg2.connect(
    database = 'alezhhahp',
    user = 'postgres', 
    password = 'zxcv1234',
    host = 'localhost',
    port = '5432' 
)

cursorSql = connectionSql.cursor()

cursorSql.execute("""
    INSERT INTO list_of_films (name, release_year, genre, rating) VALUES 
""")

connectionSql.commit()
cursorSql.close()
connectionSql.close()
