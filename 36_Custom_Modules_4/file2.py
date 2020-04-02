from file1 import GreetingCard

class BirthdayCard (GreetingCard):
    def __init__(self, recipient="Dana Ev",sender="Eyal Ch",recipient_age=0):
        super().__init__(recipient,sender)
        self._recipient_age = recipient_age
    
    def greeting_msg(self):
        print("Hello {0}, this is a greeting from {1}, you're {2} yo".format(self._recipient,self._sender,self._recipient_age))
#card = GreetingCard("Kobi","Luther")
#card.greeting_msg()