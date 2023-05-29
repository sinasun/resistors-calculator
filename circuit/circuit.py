class Circuit:
    def __init__(self):
        self.elements = []
        self.connections = []

    def add_element(self, element):
        self.elements.append(element)

    def add_connection(self, element_a, port_a, element_b, port_b):
        group_found = False

        for group in self.connections:
            if group == [element_a, port_a]:
                group.append([element_b, port_b])
                group_found = True
                
                break
            
            if group == [element_b, port_b]:
                group.append([element_a, port_a])
                group_found = True

                break

        if not group_found:
            self.connections.append([[element_a, port_a], [element_b, port_b]])

    def remove_element(self, element):
        pass

    def replace_element(self, element_a, element_b):
        pass


