
def write_results_to_file(file_name = 'file.txt', *args: tuple[float, float, float]) -> None:
    """
    Функция записывает координаты в файл
    :param file_name: str
    :param args: tuple
    :return: None
    """
    with open(file_name, 'w') as file:
        file.writelines(str(args))


def read_coordinates_from_file(file_name = 'file.txt') -> str:
    """
    Функция считывает координаты из файла
    :return: tuple[float, float, float]
    """
    with open(file_name, 'r') as file:
        file_lines = file.readline()
    return file_lines
