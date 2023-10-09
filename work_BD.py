
import psycopg2


class DBManager:
    '''Класс для подключения и работы с Базой Данных'''

    def __init__(self, host, database, user, password):
        self.conn = psycopg2.connect(host=host, database=database, user=user, password=password)

    def get_companies_and_vacancies_count(self):
        '''Получает список всех компаний и количество вакансий у каждой компании'''
        cur = self.conn.cursor()
        cur.execute("""SELECT employers.employer_id, employers.employer_name, COUNT(*)
                        FROM employers
                        JOIN vacancies ON employers.employer_id = vacancies.employer_id
                        GROUP BY employers.employer_id, employers.employer_name""")
        res = cur.fetchall()
        cur.close()
        print('\nЗагрузка списка компаний...')
        for x in res:
            print(f"Компания {x[1]}: {x[2]} вакансий")
        return

    def get_all_vacancies(self):
        '''Получает список всех вакансий с указанием названия компании,
названия вакансии, зарплаты, города и ссылки на вакансию.'''
        cur = self.conn.cursor()
        cur.execute("""SELECT *
                    FROM employers
                    JOIN vacancies ON employers.employer_id = vacancies.employer_id""")
        res = cur.fetchall()
        cur.close()
        print('\nЗагрузка списка вакансий...')
        for x in res:
            print(f"Компания: {x[1]}, Вакансия: {x[3]}, Город: {x[4]}, Зарплата ОТ: {x[5]}, Ссылка: {x[6]}")
        return

    def get_avg_salary(self):
        '''Получает среднюю зарплату по вакансиям.'''
        cur = self.conn.cursor()
        cur.execute("""SELECT AVG(salary)
                    FROM vacancies""")
        res = cur.fetchall()
        cur.close()
        print('\nЗагрузка Средней ЗП...')
        return f'Средняя зарплата: {int(res[0][0])} RUB'

    def get_vacancies_with_higher_salary(self):
        '''Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.'''
        cur = self.conn.cursor()
        cur.execute("""SELECT AVG(salary)
                    FROM vacancies""")
        average_salary = cur.fetchall()[0][0]
        cur.execute(f"""SELECT vacancies_name, salary, url FROM vacancies
                    WHERE salary > {float(average_salary)}""")
        res = cur.fetchall()
        cur.close()
        print('\nЗагрузка вакансий с ЗП выше средней...')
        for x in res:
            print(f"Вакансия: {x[0]}, Зарплата ОТ: {x[1]}, Ссылка: {x[2]}")
        return

    def get_vacancies_with_keyword(self):
        '''Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.'''
        cur = self.conn.cursor()
        search = input('Введите слово для поиска: ')
        cur.execute(f"""SELECT vacancies_name, salary, url
                    FROM vacancies
                    WHERE vacancies_name LIKE '%{search}%'""")
        res = cur.fetchall()
        cur.close()
        print(f'\nЗагрузка вакансий по слову {search}...')
        for x in res:
            print(f"Вакансия: {x[0]}, Зарплата ОТ: {x[1]}, Ссылка: {x[2]}")
        return

