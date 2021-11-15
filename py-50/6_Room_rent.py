""""
@author : Nishant Sanjay Kumbhar
@goal   : To implement hole Room rent process.
"""
import sys


def type_check_for_info(v) -> bool:
    if type(v[0]) != str or type(v[1]) != int or type(v[2]) != str or type(v[3]) != int:
        return False
    return True


class Partner_info:
    """
    This class Contains the all the information about Room Partners
    """
    def __init__(self, raj: list, prasad: list, rutwik: list, nishant: list):
        """
        This is a Constructor of Partner_info class, contains all information individually..
        :param raj: name , mobile number, locality, Adhar number : list
        :param prasad: name , mobile number, locality, Adhar number : list
        :param rutwik: name , mobile number, locality, Adhar number : list
        :param nishant: name , mobile number, locality, Adhar number : list
        """
        if type_check_for_info(raj) == False or type_check_for_info(prasad) == False or type_check_for_info(rutwik) == False or\
                type_check_for_info(nishant) == False:
            print("Bad Type Parameters For Person Info")
            sys.exit(-1)

        self.raj = raj
        self.prasad = prasad
        self.rutwik = rutwik
        self.nishant = nishant


class Room:
    """
    This is a Room class, where we take all room parameters.
    """
    def __init__(self, room_partner: Partner_info, room_rent: float, location: str, owner: str, duration_of_stay: int):
        """
        This is a Room class Constructor
        :param room_partner: it contains all the information about the persons living in the Room : Partner_info
        :param room_rent: Rent of Room per month : float or int
        :param location: Locality , where it belongs : str
        :param owner: Name of the Owner : str
        :param duration_of_stay: how many months you want to Stay : int
        """
        if type(room_partner) != Partner_info or (type(room_rent) != float and type(room_rent) != int) or \
                type(location) != str or type(owner) != str or type(duration_of_stay) != int:
            print("Bad type parameters for Room Class")
            sys.exit(-1)

        self.persons = room_partner
        self.rent = room_rent
        self.location = location
        self.owner = owner
        self.time = duration_of_stay

    def deposit(self, rent_of_room) -> float:
        rent = rent_of_room * 2
        return rent

    def show(self):
        print(self.persons.raj[2])


rj = ["Raj", 9145896235, "Baramati-Pandare", 406040985622]
py = ["Prasad", 9865784512, "Chiplun-Savarde", 706040984522]
rp = ["Rutwik", 9315468952, "Kolhapur-Radhnagri", 789645698521]
nk = ["Nishant", 1234567890, "Satara-Patan", 406056589875]
r1 = Room(Partner_info(rj, py, rp, nk), 16000, "Akurdi-Ravet", "Laxmicant Dev", 12)
print(r1)
print(r1.__dict__)
print(r1.__dict__['persons'].__dict__)
deposit = r1.deposit(16000)
print("type(deposit) : ", type(deposit))
print("Deposit will be : ", deposit)
r1.show()
