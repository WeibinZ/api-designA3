from concurrent import futures

import grpc

import objects_pb2
import services_pb2
import services_pb2_grpc


class InventoryService(services_pb2_grpc.InventoryServiceServicer):
    def __init__(self):
        book1 = objects_pb2.Book(title="Coding bootcamp", isbn="978-1-56619-909-4", genre=objects_pb2.Genre.NON_FICTION, author="Ralf Brown", publishing_year=2005)
        book2 = objects_pb2.Book(title="Romeo and Juliet", isbn="978-1-4028-9462-6", genre=objects_pb2.Genre.ROMANCE, author="William Shakespeare", publishing_year=1867)
        book3 = objects_pb2.Book(title="The Adventures of Sherlock Holmes", isbn="978-1-4028-1998-7", genre=objects_pb2.Genre.MYSTERY, author="Conan Doyle", publishing_year=1892)
        self.books = [book1, book2,book3]


    def CreateBook(self, request, context):
        print(request)
        self.books.append(request)
        return services_pb2.CreateBookResponse(success="ok")

    def GetBook(self, request, context):
        isbn = request.isbn
        print(isbn)
        for book in self.books:
            if book.isbn == isbn:
                return book

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_InventoryServiceServicer_to_server(
        InventoryService(), server)
    server.add_insecure_port('localhost:8080')
    server.start()
    print("server start")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()