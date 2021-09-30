from typing import Union

from starlette.requests import Request
from starlette.responses import Response

from ..types import FileLike
from .base import IODescriptor


class Bytes(IODescriptor):
    def openapi_request_schema(self):
        pass

    def openapi_responses_schema(self):
        pass

    async def from_http_request(self, request: Request) -> Union[bytes, FileLike]:
        pass

    async def to_http_response(self, obj: Union[bytes, FileLike]) -> Response:
        pass