# под конец второго ДЗ решил сделать небольшую декомпозицию

def str2int(value):
    try:
        result = int(value)
    except ValueError:
        result = 0
    return result
