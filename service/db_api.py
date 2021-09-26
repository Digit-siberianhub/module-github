import logging
from service.models import Base, Member

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
)

class DBApi:
    def __init__(self, url):
        self.url = self.get_valid_url(url)
        engine = create_engine(self.url)
        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=engine)
        Session = scoped_session(session_factory)
        self.session = Session()

    def get_valid_url(self, url):
        if 'postgres' in url:
            return 'postgresql+psycopg2://' + url.split('://')[-1]
        return url

    def get_member(self, username):
        member = self.session.query(Member)\
                        .filter_by(username=username)\
                        .first()
        logging.info(member)
        return member

    def set_new_counters(self, member, merged, closed):
        member.merged, member.closed = merged, closed
        self.session.commit()
        logging.info("Setting new counters")

    def create_member(self, username, merged, closed):
        member = Member(username=username, merged=merged, closed=closed)
        self.session.add(member)
        self.session.commit()
        logging.info(f"{member} CREATED")
        return member

