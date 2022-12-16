from inventory_client import InventoryClient

def get_bookTitles(client, isbnList):
    titles = []
    for isbn in isbnList:
        title = client.get_book(isbn).title
        titles.append(title)
    return titles

if __name__ == "__main__":
    client = InventoryClient("localhost", 8080)
    
    titles = get_bookTitles(client,["978-1-56619-909-4","978-1-4028-1998-7"])
    
    print(titles)