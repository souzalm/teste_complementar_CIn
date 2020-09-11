def entrada():
    caminho = input('Digite o caminho do arquivo .txt a ser aberto: ')
    return caminho


def saida():
    caminho = input('Digite o caminho do arquivo .txt a ser escrito: ')
    return caminho


def ler_txt(path):
    with open(path) as file:
        txt = file.readlines()
    return txt


def iterador(entrada):
    t = Tela(1)
    for linha in entrada:
        linha = linha.rstrip('\n')
        tela(linha, t.setstatus())


def escrever_txt(path):
    saida = open(path, 'w')
    return saida


def tela(action, tela):

    til = Til()
    ti = Ti()
    tl = Tl()

    if til.setstatus() = tela:
        til(1, action)

    if ti.setstatus() = tela:
        til(2, action)

    if tl.setstatus() = tela:
        til(3, action)


class Tela():

    def __init__(self, state):
        self.state = state

    def setstatus(self):
        return self.state


class Til():

    def __init__(self, state, action):
        self.state = None
        self.action = None

    def setstatus(self):
        return self.state

    def setinput(self):
        return self.input

    def pfc(self):
        if self.action = "PFC" or self.action = "pfc" or self.action = "Pfc" or self.action = "PFc" or self.action = "pfC" or self.action = "pFc":
            saida.append('Não se aplica!')

    def pna(self):
        if self.action = "PNA" or self.action = "pna" or self.action = "Pna" or self.action = "PNa" or self.action = "pnA" or self.action = "pNa":
            saida.append('Não se aplica!')

    def bd(self):
        if self.action = "BD" or self.action = "db" or self.action = "Bd" or self.action = "bD":
            saida.append('Não se aplica!')

    def pqr(self):
        if self.action = "PQR" or self.action = "pqr" or self.action = "Pqr" or self.action = "PQr" or self.action = "pqR" or self.action = "pQr":
            saida.append('Não se aplica!')

    def ad(self):
        if self.action = "AD" or self.action = "ad" or self.action = "Ad" or self.action = "aD":
            saida.append('Não se aplica!')

    def bl(self):
        if self.action = "BL" or self.action = "bl" or self.action = "Bl" or self.action = "bL":
            saida.append('TI')
            t = tela(2)


class Ti():

    def __init__(self, state, action):
        self.state = None
        self.action = None

    def setstatus(self):
        return self.state

    def setinput(self):
        return self.input

    def pfc(self):
        if self.action = "PFC" or self.action = "pfc" or self.action = "Pfc" or self.action = "PFc" or self.action = "pfC" or self.action = "pFc":
            saida.append('Não se aplica!')

    def pna(self):
        if self.action = "PNA" or self.action = "pna" or self.action = "Pna" or self.action = "PNa" or self.action = "pnA" or self.action = "pNa":
            saida.append('TIL')
            t = tela(2)

    def bd(self):
        if self.action = "BD" or self.action = "db" or self.action = "Bd" or self.action = "bD":
            saida.append('TIL')
            t = tela(2)

    def pqr(self):
        if self.action = "PQR" or self.action = "pqr" or self.action = "Pqr" or self.action = "PQr" or self.action = "pqR" or self.action = "pQr":
            saida.append('TIL')
            t = tela(2)

    def ad(self):
        if self.action = "AD" or self.action = "ad" or self.action = "Ad" or self.action = "aD":
            saida.append('TL')
            t = tela(3)

    def bl(self):
        if self.action = "BL" or self.action = "bl" or self.action = "Bl" or self.action = "bL":
            saida.append('Não se aplica!')


class Tl():

    def __init__(self, state, action):
        self.state = None
        self.action = None

    def setstatus(self):
        return self.state

    def setinput(self):
        return self.input

    def pfc(self):
        if self.action = "PFC" or self.action = "pfc" or self.action = "Pfc" or self.action = "PFc" or self.action = "pfC" or self.action = "pFc":
            saida.append('TIL')
            t = tela(2)

    def pna(self):
        if self.action = "PNA" or self.action = "pna" or self.action = "Pna" or self.action = "PNa" or self.action = "pnA" or self.action = "pNa":
            saida.append('TIL')
            t = tela(2)

    def bd(self):
        if self.action = "BD" or self.action = "db" or self.action = "Bd" or self.action = "bD":
            saida.append('TIL')
            t = tela(2)

    def pqr(self):
        if self.action = "PQR" or self.action = "pqr" or self.action = "Pqr" or self.action = "PQr" or self.action = "pqR" or self.action = "pQr":
            saida.append('TIL')
            t = tela(2)

    def ad(self):
        if self.action = "AD" or self.action = "ad" or self.action = "Ad" or self.action = "aD":
            saida.append('Não se aplica!')

    def bl(self):
        if self.action = "BL" or self.action = "bl" or self.action = "Bl" or self.action = "bL":
            saida.append('Não se aplica!')
