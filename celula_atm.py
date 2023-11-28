class CelulaATM:
    def __init__(self, vpi, vci, pt, clp, hec, payload):
        self.vpi = vpi
        self.vci = vci
        self.pt = pt
        self.clp = clp
        self.hec = hec
        self.payload = payload

    def __str__(self):
        return f"Célula ATM [VPI: {self.vpi}, VCI: {self.vci}, PT: {self.pt}, CLP: {self.clp}, HEC: {self.hec}, PAYLOAD: {self.payload}]"
