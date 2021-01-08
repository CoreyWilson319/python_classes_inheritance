class Phone:
    """ This is a phone class that can be used for inheritance purposes"""

    def __init__(self, phone_number, color):
        self.phone_number = phone_number
        self.color = color

    def __str__(self):
        return f"This phone belongs to {self.phone_number}"

    def call(self, other_number):
        print(f"Calling number: {other_number}")

    def text(self, other_number, message):
        print(f"Sending text to {other_number}")
        print(message)

    def open_app(self, app_name):
        print(f"Opening {app_name}")


class Android(Phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 50

    def __str__(self):
        return f"Android phone that belongs to number {self.phone_number}"

    def set_passcode(self, passcode):
        self.passcode = passcode

    def unlock_phone(self, passcode):
        if passcode == self.passcode:
            print(f"Phone Unlocked")
        else:
            print(f"Incorrect Passcode")

    def view_battery_life(self):
        print(f"Battery Life: {self.battery}")

    def charge_phone(self, charging_amount):
        self.battery += charging_amount

        if self.battery > 100:
            self.battery = 100

    def view_phone_number(self):
        print(f"Phone number: {self.phone_number}")


class IPhone(Phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.face_scan = None
        self.connect = None

    def connect_mac(self, connect):
        if self.connect == None:
            self.connect = connect

    def disconnect_mac(self, connect):
        if connect != None:
            connect = None

    def show_connection_status(self):
        if self.connect == None:
            print("Your phone is connected to nothing")
        else:
            print(f"Your phone is connected to {self.connect}")


corey_phone = Android("7345521955", "Bronze")

corey_phone.view_battery_life()
corey_phone.charge_phone(200)
corey_phone.view_battery_life()
corey_phone.view_phone_number()
corey_phone.call("734-552-5957")
corey_phone.open_app('Zoom')

g_phone = IPhone("3136573523", "White")

g_phone.show_connection_status()
g_phone.connect_mac('mac')
g_phone.show_connection_status()