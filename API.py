import requests


company_ids = [4970309, 4413765, 6080898, 3302317, 5295281, 3802070, 5156928, 2836019, 46226, 193400]


def get_job(company_ids):
    '''Функция получает с сайта HH вакансии по выбранным компаниям
     и собирает в удобный список для работы'''
    responses = []
    for id in company_ids:
        url = f'https://api.hh.ru/vacancies?employer_id={id}&per_page=10'
        employer = requests.get(url).json()
        for x in employer['items']:
            salary = 'Не указана' if x['salary'] is None else x['salary']['from']
            employer_name = 'Не указано' if x['employer'] is None else x['employer']['name']
            responses.append({'employer_id': id, 'employer_name': employer_name,
                              'vacancies': {'name': x['name'], 'city': x['area']['name'],
                                            'salary': salary, 'url': x['alternate_url']}})
    return responses

# a = get_job(company_ids)
# for x in a:
#     print(x)
