auto = {
    "marca": "ford",
    "modelo": "mustang",
    "año": 2022,
    "pais": "estados unidos",
    "color": "amarillo"
}
print(auto["modelo"])
auto["año"] = 2023
print(auto)
auto["color"] = "verde"
auto["pais"] = "peru"
print(auto)
del auto["modelo"]
auto.pop("marca")
print(auto)