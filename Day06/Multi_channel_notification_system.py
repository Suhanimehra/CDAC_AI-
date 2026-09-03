class Notifier:
    def __init__(self , sender_id , **kwargs):
        self.sender_id=sender_id

    def send(self,message):
        self.message=message
        #sel.sender_id same reASON SAMEINSTANCE ME H 
        return [f"Notifier: {self.sender_id} general broadcast: {self.message}"] # idhar notifier.message nhi use krenge kyuki khud hi function ke andar h , agar andhar hi hota to notifier.message use krte

class EmailNotifier(Notifier):
    def __init__(self, sender_id , email_server ,**kwargs):
        self.email_server=email_server
        super().__init__(sender_id, **kwargs)

    def send(self,message):

        logs = super().send(message)
        logs.insert(0, f"Email via {self.email_server} sending:{message} " )
        return logs
        
class SMSNotifier (Notifier):
    def __init__(self, sender_id , sms_gateway , **kwargs ):
        self.sms_gateway=sms_gateway
        super().__init__(sender_id, **kwargs)

    def send(self,message):
        sms_log=super().send(message)
        sms_log.insert(0, f"SMS via {self.sms_gateway} sending:{message} ")
        return sms_log
    
class HybridAlertChannel(EmailNotifier , SMSNotifier):
    def __init__(self, sender_id, email_server , sms_gateway):
        super().__init__(
            sender_id=sender_id, 
            email_server=email_server , 
            sms_gateway=sms_gateway)

    def send(self, message):

        hybrid_logs=super().send(message)

        hybrid_logs.insert(0,f"HYBRID ALERT] Initiating dual channels...")
        return hybrid_logs

alert = HybridAlertChannel(sender_id="SYS-ADMIN", email_server="smtp.cdac.in", sms_gateway="gw.acts.com")
logs = alert.send("Disk space 95%")

for log in logs:
    print(log)
print(HybridAlertChannel.__mro__)