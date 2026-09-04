import allure
import pytest

from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import GetContractDocumentRequest
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import GetTariffDocumentRequest
from tests.clients.grpc.gateway.documents.client import DocumentsGatewayGRPCTestClient
from tests.fixtures.grpc.gateway.accounts.schema import CreditCardAccountGRPCFixture
from tests.tools.allure import AllureTag, AllureEpic, AllureFeature, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_documents
@pytest.mark.regression
@pytest.mark.positive
@allure.tag(AllureTag.GRPC, AllureTag.GATEWAY_SERVICE, AllureTag.POSITIVE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.DOCUMENTS_GATEWAY_SERVICE)
class TestDocumentsGRPC:
    @allure.story(AllureStory.GET_TARIFF_DOCUMENT)
    @allure.title("[gRPC] Get tariff document")
    def test_get_tariff_document(
            self,
            function_credit_card_grpc_account: CreditCardAccountGRPCFixture,
            documents_gateway_grpc_test_client: DocumentsGatewayGRPCTestClient
    ):
        request = GetTariffDocumentRequest(account_id=function_credit_card_grpc_account.id)
        response = documents_gateway_grpc_test_client.get_tariff_document_api(request)


    @allure.story(AllureStory.GET_CONTRACT_DOCUMENT)
    @allure.title("[gRPC] Get contract document")
    def test_get_contract_document(
            self,
            function_credit_card_grpc_account: CreditCardAccountGRPCFixture,
            documents_gateway_grpc_test_client: DocumentsGatewayGRPCTestClient
    ):
        request = GetContractDocumentRequest(account_id=function_credit_card_grpc_account.id)

        response = documents_gateway_grpc_test_client.get_contract_document_api(request)
