class Circuit:
    def __init__(self):
        self.elements = []
        self.connections = []
        self.last_element = 0

    def add_element(self, element):
        self.elements.append(element)
        self.last_element += 1

    def delete_element(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def add_connection(self, element_a, port_a, element_b, port_b):
        group_found = False

        for group in self.connections:
            if [element_a, port_a] in group:
                group.append([element_b, port_b])
                group_found = True
                
                break
            
            if [element_b, port_b] in group:
                group.append([element_a, port_a])
                group_found = True

                break

        if not group_found:
            self.connections.append([[element_a, port_a], [element_b, port_b]])


    def add_connection_to_group(self, element, port, group):
        for group2 in self.connections:
            if group2 == group:
                group2.append([element, port])
                break


    def delete_connection(self, element, port):
        self.connections = [
            [item for item in group if not (item[0] == element and item[1] == port)]
            for group in self.connections
            ]
        self.connections = [[item for item in group] for group in self.connections if len(group) > 0]

    def replace_connection(self, element_a, port_a, element_b, port_b):
        updated_connections = []
        for group in self.connections:
            updated_group = []
            for item in group:
                if item[0] == element_a and item[1] == port_a:
                    updated_group.append([element_b, port_b])
                    continue
                updated_group.append(item)
            updated_connections.append(updated_group)
            self.connections = updated_connections

    def print_connections(self):
        for i, group in enumerate(self.connections):
            print(f"Connection group {i}")
            for item in group:
                print(f"{item[0].get_type()} {item[0].number} {item[1]}")
