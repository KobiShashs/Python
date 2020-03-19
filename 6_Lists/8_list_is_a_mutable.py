solar_system = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(len(solar_system))
solar_system.append("Novo")
print(len(solar_system))
solar_system += ["Python3"]
print("Python3" in solar_system)
print("Python3" not in solar_system)
print(len(solar_system))
solar_system.remove("Python3")
print("Python3" in solar_system)
print("Python3" not in solar_system)
print(len(solar_system))
