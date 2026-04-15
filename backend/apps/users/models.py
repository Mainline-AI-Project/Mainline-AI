import mongoengine as me
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Message(me.EmbeddedDocument):
    text = me.StringField(required=True)
    sender = me.StringField(choices=["user", "ai"], required=True)
    timestamp = me.DateTimeField(default=datetime.utcnow)

class Chat(me.EmbeddedDocument):
    chat_id = me.StringField(required=True)
    title = me.StringField(default="New Chat")
    messages = me.ListField(me.EmbeddedDocumentField(Message))
    created_at = me.DateTimeField(default=datetime.utcnow)
    pinned = me.BooleanField(default=False)

class User(me.Document):
    username = me.StringField(required=True, unique=True)
    email = me.EmailField(required=True, unique=True, sparse=True)
    name = me.StringField()
    password_hash = me.StringField(required=True)
    plan = me.StringField(choices=["student", "professional", "enterprise"])
    is_admin = me.BooleanField(default=False)
    chats = me.EmbeddedDocumentListField(Chat, default=[])
    created_at = me.DateTimeField(default=datetime.utcnow)

    meta = {"collection": "users"}

    def set_password(self, raw):
        self.password_hash = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self.password_hash, raw)


# import mongoengine as me
# from datetime import datetime
# from werkzeug.security import generate_password_hash, check_password_hash

# class Message(me.EmbeddedDocument):
#     text = me.StringField(required=True)
#     sender = me.StringField(choices=["user", "ai"], required=True)
#     timestamp = me.DateTimeField(default=datetime.utcnow)

# class Chat(me.EmbeddedDocument):
#     chat_id = me.StringField(required=True)  # can use UUID
#     title = me.StringField(default="New Chat")
#     messages = me.ListField(me.EmbeddedDocumentField(Message))
#     created_at = me.DateTimeField(default=datetime.utcnow)
#     pinned = me.BooleanField(default=False)

# class User(me.Document):
#     username = me.StringField(required=True, unique=True)
#     name = me.StringField()
#     password_hash = me.StringField(required=True)
#     is_admin = me.BooleanField(default=False)
#     chats = me.EmbeddedDocumentListField(Chat, default=[])
#     created_at = me.DateTimeField(default=datetime.utcnow)

#     meta = {"collection": "users"}

#     def set_password(self, raw):
#         self.password_hash = generate_password_hash(raw)

#     def check_password(self, raw):
#         return check_password_hash(self.password_hash, raw)

