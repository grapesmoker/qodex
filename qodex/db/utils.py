from sqlalchemy.exc import IntegrityError, NoResultFound


from qodex.db.settings import get_session


def get_or_create(model, session=None, **kwargs):

    session = session or get_session()
    try:
        return session.query(model).filter_by(**kwargs).one(), False
    except NoResultFound:
        created = model(**kwargs)
        try:
            session.add(created)
            session.commit()
            return created, True
        except IntegrityError:
            session.rollback()
            return session.query(model).filter_by(**kwargs).one(), False
