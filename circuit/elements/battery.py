from ..circuit_element import CircuitElement

class Battery(CircuitElement):
    def __init__(self, number, voltage):
        super().__init__("battery", number)
        self.voltage = voltage
