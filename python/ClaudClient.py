from dependencies.fbchat.fbchat import Client
from dependencies.fbchat.fbchat import Message
from dependencies.fbchat.fbchat import ThreadType
from dependencies.fbchat.fbchat import FBchatException
from dependencies.fbchat.fbchat import *

import customMessageListenerFunctions as cmlFunc

import time

import config as conf


class ClaudClient(Client):

    email = ""
    password = ""
    transDelay = 10
    threadFunc = {}

    def __init__(self, sessionCookies):

        self.email = conf.config['email']
        self.password = conf.config['password']
        self.transDelay = conf.config['transactionDelay']

        print("Claud is starting")

        # Try log in
        try:
            super().__init__(self.email, self.password, session_cookies=sessionCookies)
        except FBchatException:
            print("Cannot start Claud")
            return
    

    def claudLogin(self, sessionCookies):
        
        self.login(self.email, self.password, session_cookies=sessionCookies)
        time.sleep(self.transDelay)

        return self


    def sendMessage(self, threadId, message):

        if not self.isLoggedIn():
            self.login()

        messageId = self.send(Message(text=message), thread_id=threadId, thread_type=ThreadType.GROUP)
        time.sleep(self.transDelay)
        print("Message sent!")
        print("Message ID: ", messageId)



    def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
       
        threadName = ""
        for key, value in conf.threads.items():
            print ("Key: ", key, " Value: ", value, " Thread: ", thread_id)
            if value.strip() == thread_id:
                threadName = key.strip()
                break
        print ("Thread name: ", threadName)
        result = getattr(cmlFunc, 'onMessage_'+threadName)(self, thread_id, author_id, message_object)

