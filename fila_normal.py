class filanormal:
    codigo:int = 0
    fila = []
    clientesatendidos = []
    senhaatual:str = ''

    def gerasenhaatual(self) -> None:
        self.senhaatual = f'NM{self.codigo}'