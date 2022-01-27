"""
@author : Nishant Sanjay Kumbhar
@goal : change the domain using string operations
"""


def change_domain(current_email: str, old_domain: str, new_domain: str) -> str:
    """
    This is change_domain method to change the domain of client
    :param current_email: current e-mail address of client : str
    :param old_domain: old domain name of client : str
    :param new_domain: new domain name of client : str
    :return the new email: str
    """
    if "@" + old_domain in current_email:
        index = current_email.index("@")
        new_mail = current_email[:index] + "@" + new_domain
        return new_mail


def main():
    cur_email = input("Enter the Current E-mail Address : ")
    new_domain = input("Enter the New Domain : ")
    old = input("Enter the Old Domain : ")
    new_email = change_domain(cur_email, old, new_domain)
    print(f"Your Old E-mail address was : {cur_email} and New E-mail address is : {new_email}")


main()
