from robotics_encaps import Part, Bin, User, Log, InventoryManager
from datetime import datetime


def test_bin():
    "testing the bin class"
    bin1 = Bin(1, "B3", "34", 4)
    assert bin1.id == 1
    assert bin1.location == "B3"
    assert bin1.part_id == "34"
    assert bin1.qty_in_bin == 4


def test_part():
    "testing the part class"
    part1 = Part(34, "wrench", 5, 1)
    assert part1.id == 34
    assert part1.name == "wrench"
    assert part1.quantity == 5
    assert part1.bin_id == 1


def test_user():
    "testing the user class"
    user1 = User("marksmith@gmail.com", 22)
    assert user1.email == "marksmith@gmail.com"
    assert user1.student_num == 22


def test_log():
    "testing the log class"
    log1 = Log(20, 34, 2)
    assert log1.time == datetime
    assert log1.user_id == 20
    assert log1.part_id == 34
    assert log1.quantity == 2


def test_InventoryManager():
    "testing the InventoryManager class"
    inventory = InventoryManager()
    parts = [34, "wrench", 5, 1]
    bins = [1, "B3", 34, 4]
    logs = [20, 34, 2]
    users = ["johnsmith@gmail.com", 22]
    assert inventory.parts == parts
    assert inventory.bins == bins
    assert inventory.logs == logs
    assert inventory.users == users
