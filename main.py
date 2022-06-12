import time

from venv.data import information
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def up(url):

    # Берем словарь data, в котором прописаны логины и пароли и итерируемся по нему
    for login, password in information.items():
        count = 0
        try:
            s = Service(r"chromedriver\chromedriver.exe")
            driver = webdriver.Chrome(service=s)
            driver.maximize_window()
            driver.get(url=url)

            # Находим инпут с логином и вводим его
            input_email = driver.find_element(By.ID, "exampleInputEmail1")
            input_email.send_keys(login)

            # Находим инпут с паролем и вводим его
            input_password = driver.find_element(By.ID, "exampleInputPassword1")
            input_password.send_keys(password)

            # Жмякаем на кнопку Войти
            sign_in = driver.find_element(By.CLASS_NAME, "btn-success")
            sign_in.click()

            # Находим все кнопки, проходимся по каждой и нажимаем
            button_up = driver.find_elements(By.CLASS_NAME, "up_date")
            for i in button_up:
                i.click()
                count += 1
            print(f"Аккаунт - {login}")
            print(f"Поднятие объявлений закончено! Было поднято {count} объявлений")
            time.sleep(3)

        except Exception as _ex:
            print(_ex)
        finally:
            driver.close()
            driver.quit()


if __name__ == "__main__":
    up("https://uslugio.com/?do=users&a=login")
