from ..circuit_element import CircuitElement

class Resistor(CircuitElement):
    def __init__(self, number, resistance):
        super().__init__("resistor", number)
        self.resistance = resistance
