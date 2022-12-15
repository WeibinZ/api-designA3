from __future__ import print_function

import logging

import grpc
import services_pb2
import services_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = services_pb2_grpc.InventoryServiceStub(channel)
        response = stub.GetBook(services_pb2.BookRequest(isbn='978-1-56619-909-4'))
    print("Inventory client received: " + response.title)


if __name__ == '__main__':
    logging.basicConfig()
    run()