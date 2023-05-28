class Circuit:
    def __init__(self):
        self.elements = []
        self.connections = []

    def add_element(self, element):
        self.elements.append(element)

    def add_connection(self, element_a, port_a, element_b, port_b):
        group_found = False
        element_a_name = element_a.get_element(port_a)
        element_b_name = element_b.get_element(port_b)

        for group in self.connections:
            if element_a_name in group:
                group.append(element_b_name)
                group_found = True
                
                break
            
            if element_b_name in group:
                group.append(element_a_name)
                group_found = True

                break

        if not group_found:
            self.connections.append([element_a_name, element_b_name])
