from pprint import pprint  # pylint: disable=unused-import
from typing import Any, Dict, Tuple
import base64
from copy import deepcopy
from datetime import datetime

import pyotp
# import requests
import jwt

from settings import settings


async def jwt_encode(data: Dict[str, Any]) -> str:
    data_copy = deepcopy(data)
    # FIXME return audience parameter for jwt
    data_copy.update({
        'iss': settings.JWT.ISSUER,
        # 'aud': settings.JWT.ISSUER,
        'iat': datetime.utcnow(),
    })

    return jwt.encode(data_copy, settings.JWT.SECRET)


def jwt_decode(token):
    # FIXME return audience parameter for jwt
    return jwt.decode(token, settings.JWT.SECRET, ["HS256"])
    # return jwt.decode(token, JWT.SECRET,["HS256"], audience=JWT.ISSUER)