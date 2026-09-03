import time
import uuid

from faker import Faker
from faker.providers.python import TEnum
from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def uuid(self) -> uuid.UUID:
        return self.faker.uuid4(cast_to=None)

    def enum(self, value: type[TEnum]) -> TEnum:
        return self.faker.enum(value)

    def proto_enum(self, value: EnumTypeWrapper) -> int:
        return self.faker.random_element(value.values())

    def email(self) -> str:
        return f"{time.time()}.{self.faker.email()}"

    def category(self) -> str:
        return self.faker.random_element([
            "gas",
            "taxi",
            "tolls",
            "water",
            "beauty",
            "mobile",
            "travel",
            "parking",
            "catalog",
            "internet",
            "satellite",
            "education",
            "government",
            "healthcare",
            "restaurants",
            "electricity",
            "supermarkets",
        ])

    def last_name(self) -> str:
        return self.faker.last_name()

    def first_name(self) -> str:
        return self.faker.first_name()

    def middle_name(self) -> str:
        return self.faker.first_name()

    def phone_number(self) -> str:
        return self.faker.phone_number()

    def float(self, start: int = 1, end: int = 100) -> float:
        return self.faker.pyfloat(min_value=start, max_value=end, right_digits=2)

    def amount(self) -> float:
        return self.float(1, 1000)


fake = Fake(faker=Faker())
