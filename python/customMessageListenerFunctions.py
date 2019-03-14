import random

def onMessage_test(client, threadId, senderId, messageObject):

    if client is None:
        print('onMessage_test => No client instance')
        return

    if not senderId:
        print('onMessage_test => No senderId')
        return

    if not threadId:
        print('onMessage_test => No threadId')
        return

    if messageObject is None:
        print('onMessage_test => No messageObject')
        return

    if senderId == client.uid:
        return

    # Get sender info
    sender = client.fetchUserInfo(senderId)
    # Get sender name
    senderName = ''
    if sender:
        senderName = sender[senderId].first_name

    messagePool = ['Wala akong pake, ', "Umayos ka ", "Ano ba ", "Wag mo akong pakilaalaman ", "Bahala ka ", "Wag kang epal ", "Manahimik ka "]
    message = ""
    if not senderName:
        message = "Che, di kita kilala"
    else:
        message = messagePool[random.randint(0, len(messagePool)-1)] + senderName
    
    client.sendMessage(threadId, message)