from pprint import pprint
def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': [],
        'methods': [],
        'module': obj.__class__.__module__,
    }

    for name in dir(obj):
        attr = getattr(obj, name)
        if callable(attr) and not name.startswith("__"):
            info['methods'].append(name)
        elif not name.startswith("__"):
            info['attributes'].append(name)

    return info

# Пример использования
number_info = introspection_info(42)
pprint(number_info)

