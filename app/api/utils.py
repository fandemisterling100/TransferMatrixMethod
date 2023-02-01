from mpmath import sqrt


def get_nk(d):
    """
    This funtion return a list of tuplas: [(lambda, n, k )]
    """
    aux = []
    data = d["DATA"]
    for j, v in enumerate(data):
        if v.get("type").startswith("tabulate"):
            for j in v["data"].split("\n"):
                tupla = tuple(j.split())
                aux.append(tupla)
    return aux


def get_range_list(initial_value, final_value, pasos):
    """
    function that returns a list with the list of angles
    or wavelengths that the program will traverse.

    """
    a = initial_value
    incremento = (final_value - initial_value) / pasos
    range_list = []
    while len(range_list) < pasos:
        a = a + incremento
        range_list.append(a)
    return range_list


def get_nk_from_dielectric_fuction(epsilon_1, epsilon_2):
    """
    This funtion:
    *Calculate los valores de n and k from the dielectic funtion
    *Receives the valuos of the dielectic funtion (epsilon_1 and epsilon_2)
    * Retur a list with two values n and k
    """
    a = sqrt(epsilon_1**2 + epsilon_2**2)
    n = sqrt((epsilon_1 + a) / 2)
    k = sqrt((-epsilon_1 + a) / 2)
    return float(n), float(k)


def get_dielectric_funtion_from_nk(n, k):
    """
    This funtion:
    *Calculate los valores de epsilon_1 and epsilon_1 from the n and k
    *Receives the valuos of n and k
    * Retur a list with two values (epsilon_1 and  epsilon_2)
    """
    epsilon_1 = n**2 - k**2
    epsilon_2 = 2 * n * k
    return float(epsilon_1), float(epsilon_2)

def format_graph_data(data):
    """
    Returns just the real part of every value from 
    the data
    """
    return [round(float(value.real), 2) for value in data]