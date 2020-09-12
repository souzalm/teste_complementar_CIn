class Tela():

    def __init__(self, state):
        self.state = state

    def setstatus(self):
        return self.state


def entrada():
    caminho = input('Digite o caminho do arquivo .txt a ser aberto: ')
    return caminho


def arquivosaida():
    caminho = input('Digite o caminho do arquivo .txt a ser escrito: ')
    return caminho


def ler_txt(path):
    with open(path) as file:
        txt = file.readlines()
    return txt


def escrever_txt(path):
    saida = open(path, 'w')
    return saida


def tela(action, tela, saida):

    til = Til(1, 'None', 'None')
    ti = Ti(2, 'None', 'None')
    tl = Tl(3, 'None', 'None')

    if til.state == tela:
        til = Til(1, action, saida)
        til.pfc()
        til.pna()
        til.bd()
        til.pqr()
        til.ad()
        til.bl()

    if ti.state == tela:
        ti = Til(2, action, saida)
        ti.pfc()
        ti.pna()
        ti.bd()
        ti.pqr()
        ti.ad()
        ti.bl()

    if tl.state == tela:
        tl = Til(3, action, saida)
        tl.pfc()
        tl.pna()
        tl.bd()
        tl.pqr()
        tl.ad()
        tl.bl()


class Til():

    def __init__(self, state, action, saida):
        self.state = state
        self.action = action
        self.saida = saida

    def setstatus(self):
        return self.state

    def setinput(self):
        return self.action

    def setsaida(self):
        return self.saida

    def pfc(self):
        if self.action == "PFC" or self.action == "pfc" or self.action == "Pfc" or self.action == "PFc" or self.action == "pfC" or self.action == "pFc":
            self.saida.write('\nNao se aplica!')

    def pna(self):
        if self.action == "PNA" or self.action == "pna" or self.action == "Pna" or self.action == "PNa" or self.action == "pnA" or self.action == "pNa":
            self.saida.write('\nNao se aplica!')

    def bd(self):
        if self.action == "BD" or self.action == "db" or self.action == "Bd" or self.action == "bD":
            self.saida.write('\nNao se aplica!')

    def pqr(self):
        if self.action == "PQR" or self.action == "pqr" or self.action == "Pqr" or self.action == "PQr" or self.action == "pqR" or self.action == "pQr":
            self.saida.write('\nNao se aplica!')

    def ad(self):
        if self.action == "AD" or self.action == "ad" or self.action == "Ad" or self.action == "aD":
            self.saida.write('\nNao se aplica!')

    def bl(self):
        if self.action == "BL" or self.action == "bl" or self.action == "Bl" or self.action == "bL":
            self.saida.write('\nTI')
            t = Tela(2)


class Ti():

    def __init__(self, state, action, saida):
        self.state = state
        self.action = action
        self.saida = saida

    def setstatus(self):
        return self.state

    def setinput(self):
        return self.action

    def setsaida(self):
        return self.saida

    def pfc(self):
        if self.action == "PFC" or self.action == "pfc" or self.action == "Pfc" or self.action == "PFc" or self.action == "pfC" or self.action == "pFc":
            self.saida.write('\nNao se aplica!')

    def pna(self):
        if self.action == "PNA" or self.action == "pna" or self.action == "Pna" or self.action == "PNa" or self.action == "pnA" or self.action == "pNa":
            self.saida.write('\nTIL')
            t = Tela(2)

    def bd(self):
        if self.action == "BD" or self.action == "db" or self.action == "Bd" or self.action == "bD":
            self.saida.write('\nTIL')
            t = Tela(2)

    def pqr(self):
        if self.action == "PQR" or self.action == "pqr" or self.action == "Pqr" or self.action == "PQr" or self.action == "pqR" or self.action == "pQr":
            self.saida.write('\nNao se aplica!')
            t = Tela(2)

    def ad(self):
        if self.action == "AD" or self.action == "ad" or self.action == "Ad" or self.action == "aD":
            self.saida.write('\nTL')
            t = Tela(3)

    def bl(self):
        if self.action == "BL" or self.action == "bl" or self.action == "Bl" or self.action == "bL":
            self.saida.write('\nNao se aplica!')


class Tl():

    def __init__(self, state, action, saida):
        self.state = state
        self.action = action
        self.saida = saida

    def setstatus(self):
        return self.state

    def setinput(self):
        return self.action

    def setsaida(self):
        return self.saida

    def pfc(self):
        if self.action == "PFC" or self.action == "pfc" or self.action == "Pfc" or self.action == "PFc" or self.action == "pfC" or self.action == "pFc":
            self.saida.write('\nTIL')
            t = Tela(2)

    def pna(self):
        if self.action == "PNA" or self.action == "pna" or self.action == "Pna" or self.action == "PNa" or self.action == "pnA" or self.action == "pNa":
            self.saida.write('\nTIL')
            t = Tela(2)

    def bd(self):
        if self.action == "BD" or self.action == "db" or self.action == "Bd" or self.action == "bD":
            self.saida.write('\nTIL')
            t = Tela(2)

    def pqr(self):
        if self.action == "PQR" or self.action == "pqr" or self.action == "Pqr" or self.action == "PQr" or self.action == "pqR" or self.action == "pQr":
            self.saida.write('\nTIL')
            t = Tela(2)

    def ad(self):
        if self.action == "AD" or self.action == "ad" or self.action == "Ad" or self.action == "aD":
            self.saida.write('\nNao se aplica!')

    def bl(self):
        if self.action == "BL" or self.action == "bl" or self.action == "Bl" or self.action == "bL":
            self.saida.write('\nNao se aplica!')
