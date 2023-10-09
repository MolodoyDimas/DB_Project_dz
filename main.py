from API import get_job
from working_database import filling_table_employers, filling_table_vacancies
from work_BD import DBManager

list_vacancies = get_job()
print('Загрузка API...')
filling_table_employers()
print('Запись таблицы Компаний...')
filling_table_vacancies(list_vacancies)
print('Запись таблицы Вакансий...')

dbm = DBManager(host='localhost', database='DB_dz', user='postgres', password='65900')
print(dbm.get_companies_and_vacancies_count())
print(dbm.get_all_vacancies())
print(dbm.get_avg_salary())
print(dbm.get_vacancies_with_higher_salary())
print(dbm.get_vacancies_with_keyword())