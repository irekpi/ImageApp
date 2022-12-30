from fastapi import APIRouter
from typing import List, Type
from abc import abstractmethod, ABC
from pydantic import BaseModel


class GenericRouter(ABC):
    @abstractmethod
    def __init__(self, model: Type[BaseModel], handler):
        """Init for a router class"""

    @abstractmethod
    def set_router(self, prefix: str, dependencies: List) -> APIRouter:
        """Method for creating router based on prefix and dependencies"""


class BaseRouter(GenericRouter):
    def __init__(self, model, handler):
        self.model = model
        self.handler = handler

    def set_router(self, prefix: str = None, dependencies: List = None) -> APIRouter:
        prefix = prefix or self.model.__name__
        return APIRouter(prefix=f'/{prefix}', dependencies=dependencies)

    @abstractmethod
    def create_endpoints(self):
        ...
