class Profile:
    ##atributos##
    # adios vaquero :-(
    ##fin atributos##
    a=3
    def __init__(self,id,nickname,avatar,created_at,mail,status="online",is_premium=False): 
        self.id=id
        self.nickname=nickname
        self.avatar=avatar
        self.status=status
        self.created_at=created_at
        self.mail=mail
        self.is_premium=is_premium
    def imprimir(self):
        pass
