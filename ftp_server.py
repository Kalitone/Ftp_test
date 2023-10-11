from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "12345", ".", perm="elradfmw")
    
    handler = FTPHandler
    handler.authorizer = authorizer
    
    server = FTPServer(("0.0.0.0", 2121), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
