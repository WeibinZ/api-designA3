import grpc

import service.services_pb2 as services_pb2
import service.services_pb2_grpc as services_pb2_grpc

class InventoryClient:
    def __init__(self, address, port):
        ip = address +":"+port
        self.channel = grpc.insecure_channel(ip)
        self.stub = services_pb2_grpc.InventoryServiceStub(self.channel)

    def get_book(self, isbn):
        request = services_pb2.BookRequest(isbn=isbn)
        return self.stub.GetBook(request)