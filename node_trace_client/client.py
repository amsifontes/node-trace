from dataclasses import dataclass
from typing import Optional

import requests


@dataclass
class Client:
    service_key: Optional[str] = None
