from .utils import *

def check_short_path(circuit):

    resistors_with_both_ports = set()
    for group in circuit.connections:
        resistors = set(item[0] for item in group if item[0].get_type() == "resistor")
        if 'a' in group and 'b' in group:
            resistors_with_both_ports.update(resistors)
    
    print("short path")
    print(resistors_with_both_ports)
    if resistors_with_both_ports:
        for resistor in resistors_with_both_ports:
            circuit.remove_element(resistor)


def check_series(circuit, group):
    resistors = set(item[0] for item in group if item[0].get_type() == "resistor")

    if len(resistors) == 2:
        ports = {resistor: port for resistor, port in group}
        print("Series")
        print(ports)
        
        total_resitance = 0

        for element in ports:
            resistor = element[0]
            circuit.remove_element(resistor)

            total_resitance += resistor.resitance

        new_resistor = Resistor(len(circuit.elements) + 1, total_resitance)
        new_port = 'a'
        for element in ports:
            resistor = element[0]
            port = element[1]
            opposite_port = 'b' if port == 'a' else 'a'
            circuit.replace_connection(resistor, opposite_port, new_resistor, new_port)
            new_port = 'b'

        
            

def calculate_total_resistance(circuit):
    check_short_path(circuit) 

    for group in circuit.connections:
        check_series(circuit, group)
    
