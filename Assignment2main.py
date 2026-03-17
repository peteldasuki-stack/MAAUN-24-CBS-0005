from Assignment2models import FuelDispenser, CarWash

# Create a list of different assets
assets = [
    FuelDispenser("Dispenser 1", liters_sold=500, price_per_liter=1.2),
    FuelDispenser("Dispenser 2", liters_sold=300, price_per_liter=1.3),
    CarWash("Basic Wash", cars_washed=40, price_per_wash=7.5),
    CarWash("Premium Wash", cars_washed=25, price_per_wash=12.0)
]

# Calculate total revenue
total_revenue = 0
for asset in assets:
    total_revenue += asset.calculate_revenue()

print(f"\nTotal Station Revenue: ${total_revenue:.2f}")