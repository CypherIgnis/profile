class Profile:
    
    def __init__(self,id,nickname,avatar,created_at,mail,cellphone,password,status="online",is_premium=False): 
        self.id=id
        self.nickname=nickname
        self.avatar=avatar
        self.status=status
        self.created_at=created_at
        self.mail=mail
        self.is_premium=is_premium
        self.cellphone=cellphone
        self.password=password
    
    def imprimir(self):
        print("tu id es:", self.id)
        print("tu nickname es:", self.nickname)
        print("tu cpntraseña es:", self.password)
        print("tu telefono es:", self.cellphone)
        print("tu e-mail es:", self.mail)
        print("tu status actual es:", self.status)
