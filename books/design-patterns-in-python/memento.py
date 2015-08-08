import copy

# Memento
class Snapshot:
    def __init__(self, state):
        self.__state = state

    def get_state(self):
        return self.__state

# Originator
class CommentData:
    def __init__(self):
        self.__comments = []

    def add_comment(self, comment):
        self.__comments.append(comment)

    def show(self):
        for c in self.__comments:
            print c

    def save(self):
        return Snapshot(copy.deepcopy(self.__comments))

    def undo(self, memento):
        self.__comments = memento.get_state()

# CareTaker
if __name__ == '__main__':
    data = CommentData()
    data.add_comment('Hi')
    data.show()

    print '--------------'
    data.add_comment('Python')
    data.add_comment('Ruby')
    data.show()
    snapshot = data.save()

    print '--------------'
    data.add_comment('PHP')
    data.show()

    print '--------------'
    data.undo(snapshot)
    data.show()

