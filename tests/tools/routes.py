from enum import StrEnum


class APITestRoutes(StrEnum):
    USERS = '/api/v1/users'
    CARDS = '/api/v1/cards'
    DOCUMENTS = "/api/v1/documents"
    ACCOUNTS = '/api/v1/accounts'
    OPERATIONS = '/api/v1/operations'
