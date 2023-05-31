from circuit.elements.resistor import Resistor

def check_short_path(circuit):
    resistors_with_both_ports = set()
    for group in circuit.connections:
        resistors = set(item[0] for item in group if item[0].get_type() == "resistor")
        for resistor in resistors:
            if [resistor, 'a'] in group and [resistor, 'b'] in group:
                resistors_with_both_ports.update(resistors)
                print(f"Short Path Found for {resistor.number}")

                circuit.delete_element(resistor)
                circuit.delete_connection(resistor, 'a')
                circuit.delete_connection(resistor, 'b')

def check_series(circuit):
    for group in circuit.connections:
        resistors = [[resistor, port] for resistor, port in group if resistor.get_type() == "resistor"]
        if len(resistors) == 2 and len(group) == 2:
            print("Series Found:")
        
            total_resistance = 0
            
            for element in resistors:
                resistor = element[0]
                print(resistor.number)
                circuit.delete_element(resistor)

                total_resistance += resistor.resistance

            new_resistor = Resistor(circuit.last_element + 1, total_resistance)
            circuit.add_element(new_resistor)
            new_port = 'a'
            for element in resistors:
                resistor = element[0]
                port = element[1]
                circuit.delete_connection(resistor, port)
                opposite_port = 'b' if port == 'a' else 'a'
                circuit.replace_connection(resistor, opposite_port, new_resistor, new_port)
                new_port = 'b'
            break

def check_parallel(circuit):
    for group1 in circuit.connections:
        resistor1 = set(item[0] for item in group1 if item[0].get_type() == "resistor")

        for group2 in circuit.connections:
            if group1 != group2:
                resistor2 = set(item[0] for item in group2 if item[0].get_type() == "resistor")

                common_resistors = resistor1.intersection(resistor2)
                
                resistance_sum = 0
                if len(common_resistors) >= 2:
                    print("Parallel found: ")

                    for common_resistor in common_resistors:
                        print(common_resistor.number)
                        circuit.delete_element(common_resistor)
                        circuit.delete_connection(common_resistor, 'a')
                        if [common_resistor, 'a'] in group1:
                            group1.remove([common_resistor, 'a'])
                        if [common_resistor, 'a'] in group2:
                            group2.remove([common_resistor, 'a'])

                        circuit.delete_connection(common_resistor, 'b')
                        if [common_resistor, 'b'] in group1:
                            group1.remove([common_resistor, 'b'])

                        if [common_resistor, 'b'] in group2:
                            group2.remove([common_resistor, 'b'])


                        resistance_sum += 1/ common_resistor.resistance

                    total_resistance = 1/ resistance_sum
                
                    new_resistor = Resistor(circuit.last_element + 1, total_resistance)
                    circuit.add_element(new_resistor)
                    circuit.add_connection_to_group(new_resistor, 'a', group1)
                    circuit.add_connection_to_group(new_resistor, 'b', group2)
                    break

def calculate_total_resistance(circuit):
    while len(circuit.connections) != 2 or len(circuit.connections[0]) != 2 or len(circuit.connections[1]) != 2:
        check_short_path(circuit)
        check_series(circuit)
        check_short_path(circuit)
        check_parallel(circuit)
    for element in circuit.elements:
        if element.get_type() == "resistor":
            print(f"Total Resitance")
            print(element.resistance)

