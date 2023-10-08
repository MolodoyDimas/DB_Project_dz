from API import get_job
import psycopg2
import csv

# Таблица для Компаний, Таблица для вакансий

list_vacancies = get_job()

def only_vacancies():
    '''Функция удаляет дубликаты Компаний для удобной загрузки в таблицу'''
    list = []
    for x in list_vacancies:
        if not any(employer['employer_id'] == x['employer_id'] for employer in list):
            list.append({'employer_id': x['employer_id'], 'employer_name': x['employer_name']})
    return list


conn = psycopg2.connect(host='localhost', database='DB_dz', user='postgres', password='65900')
try:
    with conn:
        with conn.cursor() as cur:
            cur.execute('''
                CREATE TABLE employers(
	            employer_id int PRIMARY KEY,
	            employer_name varchar(30) NOT NULL);''')
            filtered_list = only_vacancies()
            for x in filtered_list:
                cur.execute(f'INSERT INTO employers VALUES (%s, %s)', (x['employer_id'], x['employer_name'],))
finally:
    conn.close()

conn = psycopg2.connect(host='localhost', database='DB_dz', user='postgres', password='65900')
try:
    with conn:
        with conn.cursor() as cur:
            cur.execute('''
            CREATE TABLE vacancies(
	        employer_id int REFERENCES employers(employer_id) NOT NULL,
	        vacancies_name varchar(100) NOT NULL,
	        city varchar(50) NOT NULL,
	        salary int,
	        url text)''')
            for x in list_vacancies:
                cur.execute(f'INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)', (
                    x['employer_id'], x['vacancies']['name'], x['vacancies']['city'], x['vacancies']['salary'],
                    x['vacancies']['url']))
finally:
    conn.close()
