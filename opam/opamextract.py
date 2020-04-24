def load(file_name):
    """
    Returns a list which containing .opam file data line by line.
    It opens file in read mode and split that line by line and
    append it to he file_data.
    """
    file_data = []
    with io.open(file_name, "r", encoding="utf-8") as f:
        file_data = [line.rstrip('\n') for line in f]
    return file_data


def get_version(file_data):
    """
    Return the value of opam-version.
    """
    for individual in file_data:
        if 'opam-version' in individual:
            version = individual.split('"')
            return version[1]


def get_maintainer(file_data):
    """
    Return the value of maintainer.
    """
    for individual in file_data:
        if 'maintainer' in individual:
            maintainer = individual.split('"')
            return maintainer[1]


def get_synopsis(file_data):
    """
    Return the value of synopsis.
    """
    for individual in file_data:
        if 'synopsis' in individual:
            synopsis = individual.split('"')
            return synopsis[1]

