"""Custom Exception type(s) for use when the Client encounters an error."""


class ClientException(Exception):
    ...


class PayloadValidationException(ClientException):
    ...
