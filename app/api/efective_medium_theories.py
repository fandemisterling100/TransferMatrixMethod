import sympy as smp
from app.api.utils import get_nk_from_dielectric_fuction


class EfectiveMediumTheories(object):
    """
    This class implements the main efective medium theories
    """

    def __init__(self):
        self.epsilon_mg = (
            1 + 0j
        )  # effective dielectric function with Maxwell Garnett model
        self.epsilon_host_mg = (
            1 + 0j
        )  # dielectric function of the host for Maxwell Garnett model
        self.volume_fractions_mg = (
            []
        )  # volume fraction of the inclusion with Maxwell Garnett model
        self.epsilon_inclusions_mg = (
            []
        )  # dielectric function of the inclusions for Maxwell Garnett model
        self.epsilon_ll = (
            1  # effective dielectric function with The Lorentz–Lorenz relation
        )
        self.epsilon_host_ll = (
            1 + 0j
        )  # dielectric function of the host for The Lorentz–Lorenz relation
        self.volume_fractions_ll = (
            0.5  # volume fraction of the inclusion with The Lorentz–Lorenz relation
        )
        self.epsilon_inclusion_ll = (
            1 + 0j
        )  # dielectric function of the inclusions for The Lorentz–Lorenz relation
        self.epsilon_br = 1 + 0j  # effective dielectric function with Bruggeman
        self.volume_fractions_br = []  # volume fraction of the phases with Bruggeman
        self.epsilon_components_br = (
            []
        )  # dielectric function of the componets for Bruggeman

    def get_maxwell_garnett(self):
        """
        This method:
        *Calculates the n and k values using the Maxwell Garnett theory
        *Receives a list of all parameters entered by the user
        * Return n and k
        """
        self.epsilon_mg = smp.symbols("epsilon_mg")
        list = []
        a = (self.epsilon_mg - self.epsilon_host_mg) / (
            self.epsilon_mg + 2 * self.epsilon_host_mg
        )

        for i, j in zip(self.volume_fractions_mg, self.epsilon_inclusions_mg):
            b = j - self.epsilon_host_mg
            c = j + (2 * self.epsilon_host_mg)
            d = -i * (b / c)
            list.append(d)

        suma = sum(list)
        e = a + suma
        solution = smp.solve(e, self.epsilon_mg)
        # print("este es el print", solution)
        effective_dielectric_functions = []
        for i in solution:
            z = complex(i)
            effective_dielectric_functions.append(z)
        if len(effective_dielectric_functions) > 1:
            if z.real >= 0 and z.imag >= 0:
                effective_dielectric_functions = z
        epsilon = effective_dielectric_functions[0]
        print("funcion dielectrica", effective_dielectric_functions)
        n_k = get_nk_from_dielectric_fuction(epsilon.real, epsilon.imag)
        return n_k

    def get_lorentz_lorenz(self):
        """
        This method:
        *Calculates the n and k values using the Lorentz Lorenz theory
        *Receives a list of all parameters entered by the user
        * Return n and k
        """
        self.epsilon_ll = smp.symbols("epsilon_ll")
        a = (self.epsilon_ll - 1) / (self.epsilon_ll + 2)
        b = (self.epsilon_inclusion_ll - 1) / (self.epsilon_inclusion_ll + 2)
        c = (self.epsilon_host_ll - 1) / (self.epsilon_host_ll - 2)
        d = 1 - self.volume_fractions_ll
        e = a - self.volume_fractions_ll * b - d * c
        solution = smp.solve(e, self.epsilon_ll)
        # print("este es el print", solution)
        effective_dielectric_functions = []
        for i in solution:
            z = complex(i)
            effective_dielectric_functions.append(z)
        if len(effective_dielectric_functions) > 1:
            if z.real >= 0 and z.imag >= 0:
                effective_dielectric_functions = z
        print("funcion dielectrica", effective_dielectric_functions)
        epsilon = effective_dielectric_functions[0]
        n_k = get_nk_from_dielectric_fuction(epsilon.real, epsilon.imag)
        return n_k

    def get_bruggeman(self):
        """
        This method:
        *Calculates the n and k values using the Bruggeman theory
        *Receives a list of all parameters entered by the user
        * Return n and k
        """
        self.epsilon_br = smp.symbols("epsilon_mg")
        list = []

        for i, j in zip(self.volume_fractions_br, self.epsilon_components_br):
            a = j - self.epsilon_br
            b = j + (2 * self.epsilon_br)
            c = a / b
            d = i * c
            list.append(d)
        suma = sum(list)
        solution = smp.solve(suma, self.epsilon_br)
        # print("este es el print", solution)
        effective_dielectric_functions = []
        for i in solution:
            z = complex(i)
            effective_dielectric_functions.append(z)
        if len(effective_dielectric_functions) > 1:
            if z.real >= 0 and z.imag >= 0:
                effective_dielectric_functions = z
        print("funcion dielectrica", effective_dielectric_functions)

        n_k = get_nk_from_dielectric_fuction(
            effective_dielectric_functions.real, effective_dielectric_functions.imag
        )
        return n_k


test = EfectiveMediumTheories()
test.epsilon_host_mg = 2
test.volume_fractions_mg = [0.7, 0.1, 0.1, 0.1, 0.1, 3, 5]
test.epsilon_inclusions_mg = [9 + 9j, 1 + 3j, 8 + 9j, 7 + 1j, 2, 9 + 10j, 9 + 3j]
test.volume_fractions_br = [0.1, 0.2, 0.4, 0.1, 0.4]
test.epsilon_components_br = [2 + 4j, 4 + 9j, 9 + 3j, 9 + 3j, 90 + 8j]
result = test.get_maxwell_garnett()
result2 = test.get_lorentz_lorenz()
result3 = test.get_bruggeman()


print(result)
print(result2)
print(result3)
