from login import login
from register import register
import helpers


def test():
    # register("Ayman|Ayman123456|18|Sajur Alatar55|0509876563|ayman@gmail.com|boy")
    print(login("Ayman|Ayman123456"))
    print(helpers.get_user_by_id(1))


test()
