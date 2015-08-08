# @see http://www.doyouphp.jp/phpdp/phpdp_02-3-10_mediator.shtml

# Mediator
class Room:
    def __init__(self):
        self.users = {}

    def login(self, user):
        user.room = self
        if user.name not in self.users:
            self.users[user.name] = user
            print "joined %s" % user.name

    def send_message(self, from_name, to_name, message):
        if to_name in self.users:
            self.users[to_name].receive_message(from_name, message)
        else:
            print "%s is not joined" % to_name

# Colleague
class User:
    def __init__(self, name):
        self.name = name
        self.room = None

    def send_message(self, to_name, message):
        self.room.send_message(self.name, to_name, message)

    def receive_message(self, from_name, message):
        print "%s >> %s: %s" % (from_name, self.name, message)

if __name__ == '__main__':
    room = Room()

    bob = User('Bob')
    john = User('John')
    alice = User('Alice')

    room.login(bob)
    room.login(john)

    bob.send_message(john.name, 'Hey John')
    john.send_message(bob.name, 'Hey Bob')

    bob.send_message(alice.name, 'Yeah')
    room.login(alice)
    alice.send_message(bob.name, 'HiHi')
