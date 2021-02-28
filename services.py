import csv
from clients.models import Client

class ClientServices:
    def __init__(self, table_name):
        self.table_name = table_name


        def create_client(self, client):
            with open(self.table_neme, mode='a') as f:
                write = csv.DictWriter(f, fieldnames=Client. schema())
                write.writerow(client. to_dict())
        
        def list_clients(self):
            with open(self. table_name, 'r') as f : 
                reader = csv.DictReader (f, fieldnames=Client. schema())

                return list(reader)