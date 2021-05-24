from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_mixins import AllFeaturesMixin, TimestampsMixin

from .conf import JsonType, ListType, base, engine, session


class BaseModel(base, AllFeaturesMixin, TimestampsMixin):
    __abstract__ = True

    def __init__(self, *args, **kwargs):
        pass


base.metadata.create_all(engine)
BaseModel.set_session(session)
