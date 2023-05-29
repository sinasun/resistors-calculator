
def get_element_from_connection(element_name):
    parts = element_name.split('_')

    element_type = parts[0]
    element_number = int(parts[1])
    element_port = parts[2]

    return element_type, element_number, element_port
