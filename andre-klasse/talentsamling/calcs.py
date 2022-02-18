import math
import dataclasses


def calc_sizes(f_t, m_d, t_b):
    '''
    Returns
    # g_p v_e isp
    '''
    g_p = m_d/t_b
    v_e = f_t/g_p
    return g_p, v_e, (v_e/9.81)


RHO = 1.2
AIR_REZ_COEF = 0.7
G = 9.81


class CGS:
    @staticmethod
    def g(x): return x/1000

    @staticmethod
    def cm(x): return x / 100


@dataclasses.dataclass()
class EngineData:
    mass_fuel: float
    mass_total: float

    time_burn: float
    mean_thrust: float

    @property
    def mass_without_fuel(self):
        return self.mass_total - self.mass_fuel


@dataclasses.dataclass()
class RocketData:
    engine: EngineData
    mass_faring: float

    n_fins: int
    fin_area: float
    diameter: float

    @property
    def radius(self):
        return self.diameter / 2

    @property
    def area(self):
        return math.pi * self.radius * self.radius + self.n_fins * self.fin_area

    @property
    def mass_without_fuel(self):
        return self.mass_faring + self.engine.mass_without_fuel

    @property
    def mass_total(self):
        return self.mass_faring + self.engine.mass_total

    @property
    def mean_mass(self):
        return (self.mass_total + self.mass_without_fuel) / 2


def calc_q(rocket: RocketData, beta):
    global G
    return math.sqrt((rocket.engine.mean_thrust - rocket.mean_mass * G)/beta)


def calc_p(rocket: RocketData, q, beta):
    return 2*beta*q/rocket.mean_mass


def calc_drag_force(vel: float, beta):
    return beta * vel * vel


def calc_free_flight_height(rocket: RocketData, drag_force: float, beta):
    global G
    return (rocket.mass_without_fuel)/(2*beta) * \
        math.log((rocket.mass_without_fuel * G + drag_force) /
                 (rocket.mass_without_fuel * G))


def calc_burning_flight_height(rocket: RocketData, drag_force, beta):
    global G
    return (-rocket.mean_mass)/(2*beta) * math.log((rocket.engine.mean_thrust - rocket.mean_mass * G - drag_force)/(rocket.engine.mean_thrust - rocket.mean_mass * G))


def calc_v_max(q, p, rocket: RocketData):
    return q * (1 - math.e**(-p*rocket.engine.time_burn))/(1 + math.e**(-p*rocket.engine.time_burn))


def calc_stabitily(center_presure, center_gravity, radius):
    return (center_presure + center_gravity)/(2*radius)


def calc_height(rocket: RocketData):
    global AIR_REZ_COEF, RHO
    beta = AIR_REZ_COEF * RHO * rocket.area / 2

    q = calc_q(rocket, beta)
    p = calc_p(rocket, q, beta)

    v_max = calc_v_max(q, p, rocket)

    drag_force = calc_drag_force(v_max, beta)

    burning_flight_height = calc_burning_flight_height(
        rocket, drag_force, beta)

    free_flight_height = calc_free_flight_height(rocket, drag_force, beta)

    return burning_flight_height + free_flight_height


if __name__ == '__main__':
    a6_4 = EngineData(CGS.g(3.5), CGS.g(14.5), 0.6, 3.7)

    # my_rocket = RocketData(3.5, 14.5, 42.8)
    my_rocket = RocketData(a6_4, CGS.g(
        57.0), 3, CGS.cm(3.5)*CGS.cm(0.5), CGS.cm(2.5))

    print(calc_height(my_rocket))

if __name__ == '__main__' and False:
    print('A6-4', calc_sizes(6, 0.0035, 0.6))
    print('B4-4', calc_sizes(4, 0.0058, 1.3))
    print('C6-7', calc_sizes(6, 0.011, 1.6))
    print('D9-7', calc_sizes(9, 0.0172, 2.1))
