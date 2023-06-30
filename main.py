
from src.find_job import HeadHunterAPI

if __name__ == "__main__":

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies()
    hh_f = hh_api.to_json()




