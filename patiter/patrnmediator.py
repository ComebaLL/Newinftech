from typing import List

# Класс посредника
class ChatMediator:
    def __init__(self):
        self.users: List[User] = []
    
    def add_user(self, user: "User"):
        self.users.append(user)
    
    def send_message(self, message: str, sender: "User"):
        for user in self.users:
            if user != sender:
                user.receive_message(message, sender)

# Класс пользователя
class User:
    def __init__(self, name: str, mediator: ChatMediator):
        self.name = name
        self.mediator = mediator
        self.mediator.add_user(self)
    
    def send_message(self, message: str):
        print(f"{self.name} send: {message}")
        self.mediator.send_message(message, self)
    
    def receive_message(self, message: str, sender: "User"):
        print(f"{self.name} get {sender.name}: {message}")

# Пример использования
mediator = ChatMediator()
user1 = User("A", mediator)
user2 = User("B", mediator)
user3 = User("C", mediator)

user1.send_message("bbb")
user2.send_message("aaa")
