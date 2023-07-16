import functions


booking_storage = {}

def test_create_booking():
    booking_storage.clear()
    functions.create_booking()
    assert len(booking_storage) == 1

def test_show_booking_list():
    booking_storage.clear()
    functions.create_booking()
    functions.show_booking_list()


def test_edit_booking_list():
    booking_storage.clear()
    functions.create_booking()
    functions.edit_booking_list()

test_create_booking()
test_show_booking_list()
test_edit_booking_list()
