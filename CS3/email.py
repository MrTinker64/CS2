class Email:
    """
    Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    >>> email = Email('hello', 'Parisa', 'Arnaud')
    >>> email.msg
    'hello'
    >>> email.sender_name
    'Parisa'
    >>> email.recipient_name
    'Arnaud' 
    """
    
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

    
class Client:
    """
    Every Client has three instance attributes: name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    >>> s = Server()
    >>> p = Client(s, 'Parisa')
    >>> a = Client(s, 'Arnaud')
    >>> a.compose('Salut!', 'Parisa')
    >>> b.inbox[0].msg
    'Salut!'
    >>> a.compose('Ca va?', 'Parisa')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'Ca va?'
    """
    def __init__(self, server, name):
        self.inbox = []
        self.name = name
        self.server = server
        server.register_client(self, name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the given recipient client."""
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this client."""
        self.inbox.append(email)


class Server:
    """
    Each Server has one instance attribute: clients (which
    is a dictionary that associates client names with
    client objects).
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """
        Take an email and put it in the inbox of the client
        it is addressed to.
        """
        self.clients[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        """
        Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        self.clients[client_name] = client

