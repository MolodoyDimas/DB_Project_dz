import requests




def get_job():
    '''Функция получает с сайта HH вакансии по выбранным компаниям
     и собирает в удобный список для работы'''
    company_ids = [4970309, 4413765, 6080898, 3302317, 5295281, 1417140, 5156928, 2836019, 46226, 1177040]
    responses = []
    for id in company_ids:
        url = f'https://api.hh.ru/vacancies?employer_id={id}&per_page=10'
        employer = requests.get(url).json()
        for x in employer['items']:
            salary = None if x['salary'] is None else x['salary']['from']
            employer_name = 'Не указано' if x['employer'] is None else x['employer']['name']
            responses.append({'employer_id': id, 'employer_name': employer_name,
                              'vacancies': {'name': x['name'], 'city': x['area']['name'],
                                            'salary': salary, 'url': x['alternate_url']}})
    return responses

# a = get_job(company_ids)
# for x in a:
#     print(x)
