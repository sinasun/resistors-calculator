from circuit.circuit import Circuit
from calculator.calculator import calculate_total_resistance
from circuit.elements.battery import Battery
from circuit.elements.resistor import Resistor


def get_int(prompt):
    while True:
        try:
            inp = int(input(prompt))
            return inp
        except ValueError:
            print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    circuit = Circuit()
    num_element = get_int("Enter number of elements in the circuit: ")

    battery_num = 0
    resistor_num = 0

    for i in range (1, num_element + 1):
        print("Input next element")

        while True:
            print("Select the element type:")
            print("1. Battery")
            print("2. Resistor")

            element_type_choice = get_int("Enter the element type number: ")
            if element_type_choice in [1,2]:
                break
            else:
                print("Invalid chioce. Please choose a number in range.")
        if element_type_choice == 1:
            battery_num += 1
            voltage = get_int("Enter battery voltage: ")
            battery = Battery(battery_num, voltage)
            circuit.add_element(battery)
            print(f"Battery {battery_num} has been created")
        else:
            element_type = "resistor"
            resistor_num += 1
            resistance = get_int("Enter resistor resistance: ")
            resistor = Resistor(resistor_num, resistance)
            circuit.add_element(resistor)
            print(f"Resistor {resistor_num} has been created")

    unconnected_ports = []

    for element in circuit.elements:
        unconnected_ports.extend([(element, 'a'), (element, 'b')])

    while unconnected_ports:
        element_start, port = unconnected_ports.pop(0)

        print(f"\nConnecting {element_start.get_element(port)}")
        
        num_connected = get_int("How many connection does this port has: ")
        for i in range(num_connected):
            element_type = ""
            while True:
                print("Select the element that is connected to:")
                print("1. Battery")
                print("2. Resistor")

                element_type_choice = get_int("Enter the element type number:")
                if element_type_choice in [1,2]:
                    break
                else:
                    print("Invalid chioce. Please choose a number in range.")
            if element_type_choice == 1:
                element_type = "battery"
            elif element_type_choice == 2:
                element_type = "resistor"

            element_number = get_int("Enter element number: ")

            connected_element = next((element for element in circuit.elements if element.get_type() == element_type and element.number == element_number))

            connected_port = input("Enter connected port (a/b): ")

            if connected_element:
                circuit.add_connection(element_start, port, connected_element, connected_port)
                if (connected_element, connected_port) in unconnected_ports:
                    unconnected_ports.remove((connected_element, connected_port))
            else:
                print("Cant find the element")
    calculate_total_resistance(circuit)
