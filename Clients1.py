import click 
from clients. services import ClientsServices
from Clients. models import Client

@click. group()
def clients():
    """ Manages the clients lifecycle"""
    pass

@clients. command()
@click. option('-n', '--name',
                type = str,
                prompt = True,
                help = 'The client name')

@click. option('-c', '--company',
                type =str,
                prompt = True,
                help = 'The client Company')

@click. option('-e', '--email',
                type = str,
                prompt = True,
                help = 'The client email')

@click. option('-p', '--postion',
                type = str,
                prompt = True,
                help = 'The client position')

@click. pass_context
def create (ctx, name, company, email, position):
    """Create a new client"""
    client = Client (name, company, email, position)
    client_service = 
    ClientsServices(ctx.obj['clients_table'])
    client_service. create_client(client)

@Clients. command()
@clients. pass_context
def list:clients(ctx):
    """List all clients"""
    cliet_services =
    ClientServices(ctx.obj['clients_table'])
    client_list = client_services. list_clients()

    click.echo('    ID  |   NAME    |   COMPANY |   EMAIL   |   POSITION')
    click. echo('*'*50)

    for client in client_list:
        print('{uid}    |   {name}  |   {company}   |   {email} |   {position}'.format(
            uid = client ['uid'],
            name = client['name'],
            company = client['company'],
            email = client('email'),
            position = client['position']
        ))


@Clients. command()
@Click. pass_context
def update (ctx, client_name):
    """Update a client"""

@Clients. command()
@Click. pass_context
def delete(ctx, client_name):
    """Delate a client"""
    pass

all = clients 



