from app import url_capture
from tud_test_base import set_keyboard_input, get_display_output


def test_hello():
    set_keyboard_input('google.com')
    url_capture()
    output = get_display_output()

    file1 = open("../Captured_Data_FROM_URL.txt", "r")
    # read file content
    readfile = file1.read()
    # closing a file
    file1.close()
    assert output == readfile
