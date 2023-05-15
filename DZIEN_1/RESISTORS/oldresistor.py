class OldResistor:
    def __init__(self,ohms):
        self._ohms = ohms

    def __repr__(self):
        return f"opornik o oporze początkowym: {self._ohms} omów"
    
    def get_ohms(self):
        return self._ohms

    def set_ohms(self,ohms):
        self._ohms = ohms
