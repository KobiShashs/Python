class GreetingCard:
    def __init__(self, recipient="Dana Ev",sender="Eyal Ch"):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print("Hello {0}, this is a greeting from {1}".format(self._recipient,self._sender))
