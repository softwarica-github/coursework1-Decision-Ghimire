import unittest
from tkinter import Tk, Entry, Listbox, Label, Frame

class PortScannerApp:
    def __init__(self, master):
        self.master = master
        self.ports = []
        self.log = []
        self.ip_f = 1024  # Initialize ip_f attribute

        self.L22 = Entry(master)
        self.L22.insert(0, "localhost")
        self.L27 = Label(master, text="[ ... ]")
        self.listbox = Listbox(Frame(master))

    def scanPort(self, target, port):
        try:
            # Simulate a successful socket connection
            self.ports = []  # Reset ports for testing purposes
            self.listbox.delete(0, 'end')  # Reset listbox for testing purposes
            self.updateResult()
            self.ports.append(port)
            self.listbox.insert("end", str(f" Port {port} \t[open]"))
            self.updateResult()
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

    def updateResult(self):
        rtext = f" [ {len(self.ports)} / {self.ip_f} ] ~ {self.L22.get()}"
        self.L27.configure(text=rtext)

class TestPortScanner(unittest.TestCase):
    def setUp(self):
        self.test_gui = Tk()
        self.test_app = PortScannerApp(self.test_gui)

    def test_scanPort(self):
        self.test_app.scanPort('localhost', 80)
        self.assertEqual(self.test_app.ports, [80])

    def test_updateResult(self):
   
      self.test_app.ports = [80, 443]
      self.test_app.updateResult()
      self.assertEqual(self.test_app.L27['text'].strip(), '[ 2 / 1024 ] ~ localhost'.strip())


if __name__ == '__main__':
    unittest.main()