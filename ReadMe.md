# Модуль для работы с телеграмом

## Руководство по запуску

1. Склонировать репозиторий

    ```git clone git@github.com:Digit-siberianhub/module-github.git```

2. Перейти в папку модуля

    ```cd module-github```

3. Установить [python3.9](https://www.python.org/downloads/)

4. Установить [pip](https://pip.pypa.io/en/stable/installation/)

5. Установить пакетный менеджер [pipenv](https://webdevblog.ru/pipenv-rukovodstvo-po-novomu-instrumentu-python/)

    ```pip install pipenv```

6. В корне создать файл **.env**

7. В файле **.env** прописать переменные окружения
    ```
    GITHUB_TOKEN="токен_тимлида_в_гитхабе"
    ORGANIZATION="название_организации"
    DATABASE_URL="sqlite:///test.db"
    ```

8. Создать виртуальное окружение через pipenv

    ```pipenv shell```

9. Установить все необходимые зависимости

    ```pipenv install --dev```

10. Запуск модуля
    ```python main.py```
