from typing import List, Optional, Dict, Any

from pydantic import BaseModel, Extra
from settings import settings




class QueryArgsPagination(BaseModel):
    limit: Optional[int] = 10
    page: Optional[int] = 1


class Login(BaseModel):
    username: str
    password: str


class LinksItemOut(BaseModel):
    href: str
    rel: Optional[str]


class LinksOut(BaseModel, extra=Extra.allow):
    self: LinksItemOut


class BaseModelExcludeNone(BaseModel):
    def dict(  # pylint: disable=useless-super-delegation
        self,
        *,
        include=None,
        exclude=None,
        by_alias: bool = False,
        skip_defaults: bool = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,  # pylint: disable=unused-argument
    ) -> Dict[str, Any]:
        return super().dict(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=True,
        )


# class ResponseLinksOut(BaseModelExcludeNone):
#     links: Optional[LinksOut]

#     class Config:
#         fields = {
#             'links': settings.LINKS,
#         }
#         allow_population_by_field_name = True


class MetaOut(BaseModelExcludeNone):
    page: int
    limit: int
    total: int


# class ResponseMetaOut(BaseModelExcludeNone):
#     meta: MetaOut

#     class Config:
#         fields = {
#             'meta': settings.META
#         }
#         allow_population_by_field_name = True


class ResponseMessageOut(BaseModelExcludeNone):
    message: str = 'Ok'


class ResponseDataItemOut(BaseModelExcludeNone):
    data: Dict[str, Any]


class ResponseDataListOut(BaseModelExcludeNone):
    data: List[Dict[str, Any]]

class ResponseToken(ResponseMessageOut):
    access_token  : str
    refresh_token : str


# class ResponseMessageLinksOut(ResponseMessageOut, ResponseLinksOut):
#     pass


# class ResponseMessageDataItemOut(ResponseMessageOut, ResponseDataItemOut):
#     pass


# class ResponseMessageDataListOut(ResponseMessageOut, ResponseDataListOut):
#     pass


# class ResponseItemOut(ResponseMessageOut, ResponseLinksOut, ResponseDataItemOut):
#     pass


# class ResponseListOut(ResponseMessageOut, ResponseLinksOut, ResponseDataListOut, ResponseMetaOut):
#     pass
