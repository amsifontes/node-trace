import logging
from typing import Optional

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Client:
    def __init__(self, application_key: str):
        self.application_key: str = application_key

    def push_event(
        self,
        event: dict,
        meta: Optional[dict] = None,
        service_key: Optional[str] = None,
    ):
        logger.info(
            "Application with key=%s pushing event=%s, meta=%s, from service_key=%s",
            self.application_key,
            event,
            meta,
            service_key,
        )
