import math

def main():
    names = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.4, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.1, 11.11, 0.42]
    ]    
    max_storage = 0
    max_cost = 0
    for name, radius, height, cost in names:
        volume = compute_volume(radius, height)
        cost_efficiency = compute_cost_efficiency(volume, cost)
        storage_efficiency = compute_storage_efficiency(radius, height)
        if cost_efficiency > max_cost:
            max_cost = cost_efficiency
            max_cost_name = name
        if storage_efficiency > max_storage:
            max_storage = storage_efficiency
            max_storage_name = name
        print(f"{name}'s storage efficiency is: {storage_efficiency: .1f}")
        print(f"{name}'s cost efficiency is: {cost_efficiency:.2f}")
    print(f"The item with the best cost efficiency is {max_cost_name} with a cost efficiency of {max_cost: 2f}. The item with the best \n storage efficiency is {max_storage_name} with a storage efficiency \n of {max_storage: .2f}.")

def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    return storage_efficiency
    
def compute_volume(radius, height):
    volume = (math.pi * (radius ** 2) * height)
    return volume

def compute_surface_area(radius, height):
    surface_area = (2 * math.pi * radius) * (radius + height)
    return surface_area

def compute_cost_efficiency (volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency

main()