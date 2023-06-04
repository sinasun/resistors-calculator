# Circuit Residence Calculator

## Table of Contents
- [Introduction](#introduction)
- [How to Use](#how-to-use)
- [Example Input and Output](#example-input-and-output)
- [Dependencies](#dependencies)
- [License](#license)

## Introduction

This Python project is designed to calculate the total resistance of an electrical circuit. It allows the user to input the components of the circuit, such as batteries and resistors, and automatically detects series and parallel resistor configurations. Additionally, the algorithm can identify short paths in the circuit.

## How to Use

1. Run the Python script `circuit_resistance_calculator.py`.

2. When prompted, enter the number of elements in the circuit.

3. For each element, you will be asked to select the element type:
   - Enter `1` for Battery.
   - Enter `2` for Resistor.

4. If you select `1` for Battery:
   - Enter the battery voltage when prompted.
   - A battery object will be created with a unique identifier.

5. If you select `2` for Resistor:
   - Enter the resistor resistance when prompted.
   - A resistor object will be created with a unique identifier.

6. After creating the elements, you will be prompted to connect them.
   - When connecting a port, enter the number of connections the port has.
   - Select the element type that is connected to the port.
   - Enter the element number of the connected element.
   - Enter the connected port (a/b) for the selected element.

7. Once the connections are established, the program will calculate the total resistance of the circuit.

8. The program will display any parallel resistor configurations found and the total resistance of the circuit.

## Example Input and Output

Suppose we have the following input:

```bash
Enter number of elements in the circuit: 3

Input next element
Select the element type:
1. Battery
2. Resistor
Enter the element type number: 1
Enter battery voltage: 10
Battery 1 has been created

Input next element
Select the element type:
1. Battery
2. Resistor
Enter the element type number: 2
Enter resistor resistance: 8
Resistor 1 has been created

Input next element
Select the element type:
1. Battery
2. Resistor
Enter the element type number: 2
Enter resistor resistance: 10
Resistor 2 has been created

Connecting battery_1_a
How many connections does this port have: 2
Select the element that is connected to:
1. Battery
2. Resistor
Enter the element type number: 2
Enter element number: 1
Enter connected port (a/b): a
Select the element that is connected to:
1. Battery
2. Resistor
Enter the element type number: 2
Enter element number: 2
Enter connected port (a/b): a

Connecting battery_1_b
How many connections does this port have: 2
Select the element that is connected to:
1. Battery
2. Resistor
Enter the element type number: 2
Enter element number: 1
Enter connected port (a/b): b
Select the element that is connected to:
1. Battery
2. Resistor
Enter the element type number: 2
Enter element number: 2
Enter connected port (a/b): b
```

The output will be:

```bash
Parallel found:
2
1
Total Resistance: 4.444444444444445
```

## Dependencies

This project does not have any external dependencies. It is written in Python and can be executed using a Python interpreter.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it according to your needs.

