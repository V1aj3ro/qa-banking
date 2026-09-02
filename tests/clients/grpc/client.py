import grpc


class GRPCTestClient:
    def __init__(self, channel: grpc.Channel):
        self.channel = channel



