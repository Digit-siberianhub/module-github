# Модуль для работы с телеграмом

## Руководство по запуску

1. Для начала нужно получить токен для GitHub -> [инструкция](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

2. Склонировать репозиторий

    ```
    git clone git@github.com:Digit-siberianhub/module-github.git
    ```

3. Перейти в папку модуля

    ```
    cd module-github
    ```

4. Установить [python3.9](https://www.python.org/downloads/)

5. Установить [pip](https://pip.pypa.io/en/stable/installation/)

6. Установить пакетный менеджер [pipenv](https://webdevblog.ru/pipenv-rukovodstvo-po-novomu-instrumentu-python/)

    ```
    pip install pipenv
    ```

7. В корне создать файл **.env**

8. В файле **.env** прописать переменные окружения
    ```
    GITHUB_TOKEN="токен_тимлида_в_гитхабе"
    ORGANIZATION="название_организации"
    DATABASE_URL="sqlite:///test.db"
    ```

9. Создать виртуальное окружение через pipenv

    ```
    pipenv shell
    ```

10. Установить все необходимые зависимости

    ```
    pipenv install --dev
    ```

11. Запуск модуля

    ```
    python main.py
    ```
