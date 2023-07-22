import argparse
import logging
import random
import uuid
import time
from datetime import datetime
from typing import Optional

import client

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


c = client.Client(application_key="my-application")


def main(num_steps: int):
    """Simulate random calls between services, represented as functions."""
    func_registry = [service_1, service_2, service_3, service_4]
    logger.info("num_steps: %i", num_steps)
    request: dict[str, str] = {"message": "foo"}
    response: Optional[dict] = None
    for step in range(num_steps):
        logger.info("step: %i", step)
        func = random.choice(func_registry)
        if step == 0:
            # first request - create a unifying id
            request_id: str = uuid.uuid4()
            request["request_id"] = request_id
            request["request_initiated_time"] = datetime.now()
        else:
            # each response is the request for the next service.
            request = response

        c.push_event(
            event=request, meta={"type": "send"}, service_key="my-application.main"
        )
        response = func(request)
        c.push_event(
            event=response, meta={"type": "receive"}, service_key="my-application.main"
        )

    logger.info("Original caller received response: %s", response)


def service_1(request: dict) -> dict:
    logger.info("service_1 received request: %s", request)
    logger.info("request received at %s", datetime.now())
    c.push_event(
        event=request,
        meta={"type": "receive"},
        service_key="my-application.main.service-1",
    )
    time.sleep(0.1)
    request["request_initiated_time"] = datetime.now()
    c.push_event(
        event=request,
        meta={"type": "send"},
        service_key="my-application.main.service-1",
    )
    return request


def service_2(request: dict) -> dict:
    logger.info("service_2 received request: %s", request)
    logger.info("request received at %s", datetime.now())
    c.push_event(
        event=request,
        meta={"type": "receive"},
        service_key="my-application.main.service-2",
    )
    time.sleep(0.1)
    request["request_initiated_time"] = datetime.now()
    c.push_event(
        event=request,
        meta={"type": "send"},
        service_key="my-application.main.service-2",
    )
    return request


def service_3(request: dict) -> dict:
    logger.info("service_3 received request: %s", request)
    logger.info("request received at %s", datetime.now())
    c.push_event(
        event=request,
        meta={"type": "receive"},
        service_key="my-application.main.service-3",
    )
    time.sleep(0.1)
    request["request_initiated_time"] = datetime.now()
    c.push_event(
        event=request,
        meta={"type": "send"},
        service_key="my-application.main.service-3",
    )
    return request


def service_4(request: dict) -> dict:
    logger.info("service_4 received request: %s", request)
    logger.info("request received at %s", datetime.now())
    c.push_event(
        event=request,
        meta={"type": "receive"},
        service_key="my-application.main.service-4",
    )
    time.sleep(0.1)
    request["request_initiated_time"] = datetime.now()
    c.push_event(
        event=request,
        meta={"type": "send"},
        service_key="my-application.main.service-4",
    )
    return request


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Trace transactions a specific number of steps"
    )
    ap.add_argument("num_steps", type=int)
    args = ap.parse_args()
    main(num_steps=args.num_steps)
