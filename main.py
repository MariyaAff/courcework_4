from src.find_job import HeadHunterAPI, JSONSaver
from src.find_job import SuperJobAPI


def main():
    sj_api = SuperJobAPI("python")
    hh_api = HeadHunterAPI("python")
    keyword = input("Введите слово для поиска")
    vacancies = []
    for api in (hh_api, sj_api):
        api.get_vacancies("python")
        vacancies.append(api.get_formatted_vacancies())

    js = JSONSaver(keyword, vacancies)
    vacancies = []
    while True:
        input('1 вывести все \n 2 отсортировать или exit')
        if 1:
            vacancies = js.select_all()
            print(vacancies)
        if 2:
            vacancies = js.sorted_by()
            print(vacancies)
        if "exit":
            break
        for v in vacancies:
            print(v)


if __name__ == "__main__":
    main()
