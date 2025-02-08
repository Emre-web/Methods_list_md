# Veri tiplerini listele
data_types = {
    "List": list,
    "Set": set,
    "String": str,
    "Tuple": tuple,
    "Dictionary": dict
}

# "__" ile başlayan özel metotları filtrele
methods = {name: [m for m in dir(dtype) if not m.startswith("__")] for name, dtype in data_types.items()}

# Maksimum uzunluğu belirle
max_length = max(len(m) for m in methods.values())

# Markdown dosyasına yaz
with open("methods.md", "w") as file:
    headers = ["List Methods", "Set Methods", "String Methods", "Tuple Methods", "Dictionary Methods"]
    
    # Başlık satırını yaz
    file.write("| " + " | ".join(headers) + " |\n")
    file.write("|" + "|".join(["-" * len(h) for h in headers]) + "|\n")

    # Her satırı oluştur ve yaz
    for i in range(max_length):
        row = [
            methods[category][i] if i < len(methods[category]) else "" for category in methods
        ]
        file.write("| " + " | ".join(row) + " |\n")

print("methods.md dosyası oluşturuldu! 🎯")
