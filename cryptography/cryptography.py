# Learning how does cryptograpy works.......
# this program can encode and decode messages.... 
def machine():
    keys ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%^&*()_+-*{|:"}<>?~`=[];,./! '
    values = keys[-1] + keys[0:-1]

    encryptDict = dict(zip(keys,values))
    decryptDict = dict(zip(values,keys))
    
    message= input("please enter your secrete message:")
    mode = input("please enter the mode : press (E) for Encode OR (D) for Decode:")
    
    if mode=='E':
        newMessage= ''.join([encryptDict[letter]
            for letter in message])
    elif mode == 'D':
        newMessage= ''.join([decryptDict[letter]
            for letter in message])
    elif mode !='E''D':
        newMessage = print("please enter a correct choice")
    return newMessage
print(machine())