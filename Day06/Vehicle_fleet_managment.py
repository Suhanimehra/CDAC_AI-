class Vehicle:

    def __init__(self , make , model , fuel_capacity):
        self.make=make
        self.model=model
        self.fuel_capacity=fuel_capacity

    def calculate_range(self,fuel_efficiency):
        return self.fuel_capacity* fuel_efficiency

    def get_description(self):
        return  f"Truck: {self.make} {self.model} carrying {self.cargo_load} tons"

class DeliveryTruck(Vehicle):

    def __init__(self, make, model, fuel_capacity , cargo_load):
        super().__init__(make, model, fuel_capacity)

        self.cargo_load=cargo_load

    def calculate_range(self, fuel_efficiency):
        # base_range=super().calculate_range(fuel_efficiency)
        # adjusted_range=base_range *(1.0 - 0.1 * self.cargo_load)
        
        # return adjusted_range
        return super().calculate_range(fuel_efficiency) * (1.0 - 0.1 * self.cargo_load)

    def get_description(self):
        return super().get_description()
        
        
truck = DeliveryTruck("Volvo", "FH16", 300.0, 2.0)

print(truck.calculate_range(5.0))
print(truck.get_description())