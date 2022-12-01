class Profile:
    
    def __init__(self,id,nickname,avatar,created_at,mail,cellphone,password,status="online",is_premium=False): 
        self.__id=id
        self.__nickname=nickname
        self.__avatar=avatar
        self.__status=status
        self.__created_at=created_at
        self.__mail=mail
        self.__is_premium=is_premium
        self.__cellphone=cellphone
        self.__password=password
    
    def get__id(self):
        return self.__id
    
    def set__id(self,value):
        self.__id = value
   
    def get__nickname(self):
        return self.__nickname
    
    def set__nickname(self,value):
        self.__nickname = value
    
    def get__avatar(self):
        return self.__avatar
    
    def set__avatar(self,value):
        self.__avatar = value
    
    def get__status(self):
        return self.__status
    
    def set__status(self,value):
        self.__status = value
    
    def get__created_at(self):
        return self.__created_at
    
    def set__created_at(self,value):
        self.__created_at = value
        
    def get__mail(self):
        return self.__mail
    
    def set__mail(self,value):
        self.__mail = value
        
    def get__is_premium(self):
        return self.__is_premium
    
    def set__is_premium(self,value):
        self.__is_premium = value
        
    def get__cellphone(self):
        return self.__cellphone
    
    def set__cellphone(self,value):
        self.__cellphone = value
        
    def get__password(self):
        return self.__password
    
    def set__password(self,value):
        self.__password = value
        
    
    def imprimir(self):
        print("tu id es:", self.id)
        print("tu nickname es:", self.nickname)
        print("tu cpntraseña es:", self.password)
        print("tu telefono es:", self.cellphone)
        print("tu e-mail es:", self.mail)
        print("tu status actual es:", self.status)
