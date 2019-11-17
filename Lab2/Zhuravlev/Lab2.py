class Car:
    def __init__(self, model, max_speed, cost):
        self.model = model
        self.max_speed = max_speed
        self.cost = cost
        self.fuel = []

    def add_fuel(self, name):
        self.fuel.append(name)

    def __repr__(self):
        return "{0} has max speed {2} km/h and cost starts from {1} rubles"\
            .format(self.model, self.cost, self.max_speed)

    def __str__(self):
        result = 'Car can use next fuel:\n'
        for val in self.fuel:
            result += val + '\n'
        return result


x = Car('Toyota Camry', 240, 3200000)
x.add_fuel('patrol')
x.add_fuel('diesel')
print(repr(x))
print(str(x))
