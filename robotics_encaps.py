from datetime import datetime


class Bin:
    """ Represents a storage bin
    Attrs:
        bin_id(int): shows the id of the bin
        location(str): shows the bin's location
        part_id(str): shows id of a single Part object
        qty_in_bin(int): shows how many of said Part is in the bin
    """
    def __init__(self, bin_id: int, location: str, part_id: int, qty_in_bin: int):
        "Initializes description of the bin"
        self._id = bin_id
        self._location = location
        self._part_id = part_id
        self._qty_in_bin = qty_in_bin

    def get_id(self):
        return self._id

    def set_id(self, value: int):
        assert value >= 0
        self._id = value

    def get_location(self):
        return self._location

    def set_location(self, value: str):
        self._location = value

    def get_part_id(self):
        return self._part_id

    def set_part_id(self, value: int):
        assert value >= 0
        self._part_id = value

    def get_qty_in_bin(self):
        return self._qty_in_bin

    def set_qty_in_bin(self, value: int):
        assert value >= 0
        self._qty_in_bin = value


class Part:
    """ Represents a part
    Attrs:
        part_id(int): shows the id of the part
        name(str): shows the part's name
        quantity(int): show how much of that part is in the bin
        bin_id(int): show the id of a single Bin object
    """
    def __init__(self, part_id: int, name: str, quantity: int, bin_id: int):
        "Initializes description of the part"
        self._id = part_id
        self._name = name
        self._quantity = quantity
        self._bin_id = bin_id

    def get_id(self):
        return self._id

    def set_id(self, value: int):
        assert value >= 0
        self._id = value

    def get_name(self):
        return self._name

    def set_name(self, value: str):
        self._name = value

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, value: int):
        assert value >= 0
        self._quantity = value

    def get_bin_id(self):
        return self._bin_id

    def set_bin_id(self, value: int):
        assert value >= 0
        self._bin_id = value


class User:
    """ Represents a User's info
    Attrs:
        email(str): shows the student's email
        student_num(int): shows the student's number
    """
    def __init__(self, email: str, student_num: int):
        "Initializes description of the student's information"
        self._email = email
        self._student_num = student_num

    def get_email(self):
        return self._email

    def set_email(self, value: str):
        self._email = value

    def get_student_num(self):
        return self._student_num

    def set_student_num(self, value: str):
        self._student_num = value


class Log:
    """ Represents a user login
    Attrs:
        time(datetime): shows the time of login
        user_id(int): shows the user's id
        part_id(int): show's the id of the part being logged out
        quantity(int): shows how much of a part was logged out
    """
    def __init__(self, time: datetime, user_id: int, part_id: int, quantity: int):
        "Initializes description of the log data"
        self.time = time
        self._user_id = user_id
        self._part_id = part_id
        self._quantity = quantity

    def get_user_id(self):
        return self._user_id

    def set_user_id(self, value: int):
        assert value >= 0
        self._user_id = value

    def get_part_id(self):
        return self._part_id

    def set_part_id(self, value: int):
        assert value >= 0
        self._part_id = value

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, value: int):
        assert value >= 0
        self._quantity = value


class InventoryManager:
    """ Represents an inventory
    parts(List): Shows a list of all parts
    bins(List): Shows a list of all bins
    logs(List): Shows a list of all the logs
    users(List): Shows a list of all users
    """
    def __init__(self):
        "Initializes description of the inventory data"
        self.parts = []
        self.bins = []
        self.logs = []
        self.users = []
