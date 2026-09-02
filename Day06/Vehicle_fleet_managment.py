class Vehicle:

    def __init__(self , make , model , fuel_capacity):
        self.make=make
        self.model=model
        self.fuel_capacity=fuel_capacity

    def calculate_range(self,fuel_efficiency):
        return self.fuel_capacity* fuel_efficiency

    def get_description(self):
        return f"Vehicle: {self.make} {self.model}"

class DeliveryTruck(Vehicle):

    def __init__(self, make, model, fuel_capacity , cargo_load):
        super().__init__(make, model, fuel_capacity)

        self.cargo_load=cargo_load

    def calculate_range(self, fuel_efficiency):
        return super().calculate_range(fuel_efficiency)

    def get_description(self):
        return super().get_description()