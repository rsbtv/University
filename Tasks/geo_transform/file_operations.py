
def write_results_to_file(*args: tuple[float, float, float]) -> None:
    """
    Функция записывает координаты в файл
    :param args: tuple
    :return: None
    """
    with open('file.txt', 'w') as file:
        file.writelines(str(args))

def read_coordinates_from_file() -> tuple[float, float, float]:
    """
    Функция считывает координаты из файла
    :return: tuple[float, float, float]
    """
    with open('file.txt', 'r') as file:
        file_lines = file.readlines() # TODO: FIX THAT
    return file_lines
