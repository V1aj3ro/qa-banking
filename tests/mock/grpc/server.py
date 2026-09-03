import asyncio
from concurrent import futures

import grpc
from grpc_reflection.v1alpha import reflection

from contracts.services.accounts import accounts_service_pb2_grpc, accounts_service_pb2
from contracts.services.cards import cards_service_pb2, cards_service_pb2_grpc
from contracts.services.documents.contracts import contracts_service_pb2_grpc, contracts_service_pb2
from contracts.services.documents.receipts import receipts_service_pb2_grpc, receipts_service_pb2
from contracts.services.documents.tariffs import tariffs_service_pb2_grpc, tariffs_service_pb2
from contracts.services.operations import operations_service_pb2_grpc, operations_service_pb2
from contracts.services.users import users_service_pb2, users_service_pb2_grpc
from tests.config import test_settings
from tests.mock.grpc.api.accounts import AccountsMockService
from tests.mock.grpc.api.cards import CardsMockService
from tests.mock.grpc.api.documents.contracts import ContractsMockService
from tests.mock.grpc.api.documents.receipts import ReceiptsMockService
from tests.mock.grpc.api.documents.tariff import TariffsMockService
from tests.mock.grpc.api.operations import OperationsMockService
from tests.mock.grpc.api.users import UsersMockService


async def serve():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port(test_settings.mock_grpc_server.url)

    users_service_pb2_grpc.add_UsersServiceServicer_to_server(UsersMockService(), server)
    cards_service_pb2_grpc.add_CardsServiceServicer_to_server(CardsMockService(), server)
    accounts_service_pb2_grpc.add_AccountsServiceServicer_to_server(AccountsMockService(), server)
    operations_service_pb2_grpc.add_OperationsServiceServicer_to_server(OperationsMockService(), server)
    contracts_service_pb2_grpc.add_ContractsServiceServicer_to_server(ContractsMockService(), server)
    receipts_service_pb2_grpc.add_ReceiptsServiceServicer_to_server(ReceiptsMockService(), server)
    tariffs_service_pb2_grpc.add_TariffsServiceServicer_to_server(TariffsMockService(), server)

    reflection.enable_server_reflection(
        (
            reflection.SERVICE_NAME,
            users_service_pb2.DESCRIPTOR.services_by_name['UsersService'].full_name,
            cards_service_pb2.DESCRIPTOR.services_by_name['CardsService'].full_name,
            tariffs_service_pb2.DESCRIPTOR.services_by_name['TariffsService'].full_name,
            receipts_service_pb2.DESCRIPTOR.services_by_name['ReceiptsService'].full_name,
            accounts_service_pb2.DESCRIPTOR.services_by_name['AccountsService'].full_name,
            contracts_service_pb2.DESCRIPTOR.services_by_name['ContractsService'].full_name,
            operations_service_pb2.DESCRIPTOR.services_by_name['OperationsService'].full_name
        ),
        server
    )

    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())
