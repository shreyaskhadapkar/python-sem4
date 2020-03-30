with open("recipent.txt",'r',encoding = 'utf-8') as recipent_file:
    with open("content.txt","r", encoding='utf-8') as context_file:
        message = context_file.read()
 
        for recipient in recipent_file:
            mail = "Hey " + recipient  + "Hope you are having a good day\n"+ message
 
            with open(recipient.strip() + ".txt", "w", encoding='utf-8') as mail_file:
                mail_file.write(mail)