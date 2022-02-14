from privemail import sender
from privemail import password 
import random
import smtplib 
class SecretSanta:
    def __init__(self):
        self.info = {}
        self.selection = {}
        self.participants = 0 
        self.budget = 0 

    def neededinfo(self):
        self.participants = int(input('How many participants will be participating?: '))
        self.budget = int(input('What is the budget discussed for Secret Santa?: $'))

        while len(self.info) < self.participants:
            name = input('What is the name of the participant?: ')
            if name in self.info:
                print('Name already used, use a nickname')
                continue 
            email = input('What is their email?: ')
            address = input('What is their address?: ')
            self.info[name]= [email, address]

    def assign(self):
        choices = [name for name in self.info]
        for person in self.info: 
            secretperson = random.choice(choices) 
            while secretperson == person: 
                secretperson = random.choice(choices)
                if secretperson == person: 
                    continue 
                break
            self.selection[person] = secretperson
            ind = choices.index(secretperson)
            choices.pop(ind)

    def sendemails(self):
        server = smtplib.SMTP('smtp.gmail.com')
        for person in self.selection:
            server.connect('smtp.gmail.com', '587')
            server.ehlo()
            server.starttls()
            server.login(sender, password)
            receiver = self.info[person][0]
            secretperson_address = self.info[self.selection[person]][1]
            message = 'Hi Secret Santa {}! \nThe budget this season is: ${} \nYou are gifting: {} \nThis is their address: {}. \nHappy Holidays!!!'.format(person, self.budget, self.selection[person],  secretperson_address)
            server.sendmail(sender, receiver, message)
            server.quit()


    def start(self):
        self.neededinfo()
        self.assign()
        self.sendemails()
        
if  __name__ == '__main__':
    hohoho = SecretSanta()
    hohoho.start()
