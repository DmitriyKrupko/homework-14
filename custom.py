class CustomObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

def create_object(field_names, class_name):
    if class_name == "CustomObject":
        field_values = {name: 0 for name in field_names if isinstance(name, str)}
        return CustomObject(**field_values)
    else:
        raise ValueError(f"Класс '{class_name}' не поддерживается.")

if __name__ == "__main__":
    fields = ["field1", "field2", "field3"]  # Текстовые элементы
    obj = create_object(fields, "CustomObject")

    print(vars(obj))