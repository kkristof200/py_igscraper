# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# Pip
from jsoncodable import JSONCodable

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------- class: CoreIGUserData --------------------------------------------------------- #

class CoreIGUserData(JSONCodable):

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        d: dict
    ):
        self.id = d['id']
        self.username = d['username']
        self.url = 'https://www.instagram.com/{}'.format(self.username)


# ---------------------------------------------------------------------------------------------------------------------------------------- #