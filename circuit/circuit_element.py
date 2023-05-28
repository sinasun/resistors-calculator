class CircuitElement:
    def __init__(self, element_type, number):
        self.element_type = element_type
        self.number = number

    def get_element(self, port):
        return f"{self.element_type}_{self.number}_{port}"

    def get_type(self):
        return self.element_type

