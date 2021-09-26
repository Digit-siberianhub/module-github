import logging
from time import sleep

import service.credentials as creds
from service.core_api import CoreAPI
from service.github import GitHub
from service.db_api import DBApi


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
)

TIME = 10
git = GitHub(creds.ORGANIZATION, creds.GITHUB_TOKEN)
db = DBApi(creds.DATABASE_URL)
core = CoreAPI(
    'GitHub',
    'Модуль для работы с гитхабом',
    'Инструмент'
)

def scheduled(wait_for):
    while True:
        for username in git.get_members():
            merged_count, closed_count = 0, 0
            for repo in git.get_repos():
                for pull in git.get_pulls(repo, username):
                    if pull['merged_at']:
                        merged_count += 1
                    if pull['closed_at']:
                        closed_count += 1

            # Так как все пуллы при слиянии считаются закрытыми, то нужно:
            closed_count = closed_count - merged_count

            member = db.get_member(username)
            logging.info(f'{member} merged_count: {merged_count} closed_count: {closed_count}')
            if not member:
                member = db.create_member(username, merged=merged_count, closed=closed_count)
            if [member.merged, member.closed] != [merged_count, closed_count]:
                core.send_data(username, merged_count - closed_count)
                db.set_new_counters(member, merged_count, closed_count)

        sleep(wait_for)


if __name__ == '__main__':
    logging.info('GITHUB MODULE STARTED')
    core.register_module()
    scheduled(TIME)
