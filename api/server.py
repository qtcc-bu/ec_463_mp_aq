import numpy as np
import time
class Message:
    def __init__(self,time,user,message):
        self.time = time
        self.user = user
        self.message = message
    def __str__(self):
        print('###',self.user,'###')
        print(self.message)
        return ''
class ServerState:
    def __init__(self):
        print('Server Initialized!')
        self.__user_pass_token_dict = {} # in format: {email:(name,password,token)}
        self.__user_email_dict = {} # in format: {name:email}
        self.__token_name_dict = {} # in format {token:name}
        self.__conversation_dict = {} # in format: {[token1,token2]:list[messages]}
        self.__blocked_by_dict = {} # in format: {user:list[people who have blocked them]}
    def sign_up(self,email,name,password):
        if email in self.__user_pass_token_dict:
            print('User already registered!')
            return False
        new_user_token = np.random.rand()
        self.__user_pass_token_dict.update({email:(name,password,new_user_token)})
        self.__user_email_dict.update({name:email})
        self.__token_name_dict.update({new_user_token:name})
        print('Successfully registered!')
        return True
    def login(self,email,password):
        # tries to find user in user database
        if email in self.__user_pass_token_dict:
            # sees if password matches given login
            if self.__user_pass_token_dict[email][1] == password:
                # Returns user's unique token
                return self.__user_pass_token_dict[email][2]
        # if login fails, returns False
        return False
    def _get_email_from_name(self,name):
        if name in self.__user_email_dict:
            return self.__user_email_dict[name]
        return False
    def _get_token_from_email(self,email):
        if email in self.__user_pass_token_dict:
            return self.__user_pass_token_dict[email][2]
        return False
    def _get_token_from_name(self,name):
        email = self._get_email_from_name(name)
        if email is not False:
            return self._get_token_from_email(email)
        return False
    def start_conversation(self,token1,token2):
        #token_duo = tuple([token1,token2].sort())
        token_duo = tuple(sorted([token1,token2]))
        self.__conversation_dict.update({token_duo:[]})
        return True
    def find_convo_from_email(self,user_token,search_email):
        recipient_token = self._get_token_from_email(search_email)
        #token_duo = tuple([user_token,recipient_token].sort())
        token_duo = tuple(sorted([user_token,recipient_token]))
        if token_duo in self.__conversation_dict:
            return self.__conversation_dict[token_duo]
        return False
    def find_convo_from_name(self,user_token,search_name):
        recipient_token = self._get_token_from_name(search_name)
        #token_duo = tuple([user_token,recipient_token].sort())
        token_duo = tuple(sorted([user_token,recipient_token]))
        if token_duo in self.__conversation_dict:
            return self.__conversation_dict[token_duo]
        return False
    def _get_name_from_token(self,token):
        if token in self.__token_name_dict:
            return self.__token_name_dict[token]
        return False
    def send_message_to_convo(self,user_token,name,email,use_email,message):
        if use_email:
            recipient_token = self._get_token_from_email(email)
        else:
            recipient_token = self._get_token_from_name(name)
        if self.check_if_blocked(user_token,recipient_token):
            return False
        new_message = Message(time.time(),self._get_name_from_token(user_token),message)
        #token_duo = tuple([user_token,recipient_token].sort())
        token_duo = tuple(sorted([user_token,recipient_token]))

        if token_duo not in self.__conversation_dict:
            self.start_conversation(user_token,recipient_token)
        convo_list = self.__conversation_dict[token_duo]
        convo_list.append(new_message)
        self.__conversation_dict.update({token_duo:convo_list})
        return True
    def block_user_token(self,user_token,block_user_token):
        if block_user_token not in self.__blocked_by_dict:
            self.__blocked_by_dict.update({block_user_token:[]})
        blocked_list = self.__blocked_by_dict[block_user_token]
        blocked_list.append(user_token)
        self.__blocked_by_dict.update({block_user_token:blocked_list})
        return True
    def check_if_blocked(self,send_user_token,receiver_user_token):
        if send_user_token in self.__blocked_by_dict:
            if receiver_user_token in self.__blocked_by_dict[send_user_token]:
                return True
        return False
    def temp(self):
        return self.__token_name_dict