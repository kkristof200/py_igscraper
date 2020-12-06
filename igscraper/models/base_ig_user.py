# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# Local
from .core_ig_user_data import CoreIGUserData

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------------------- class: BaseIGUser ----------------------------------------------------------- #

class BaseIGUser(CoreIGUserData):

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        d: dict
    ):
        super().__init__(d)

        self.full_name = d['full_name']

        self.is_private = d['is_private']
        self.is_verified = d['is_verified']

        self.profile_pic_url = d['profile_pic_url']


# ---------------------------------------------------------------------------------------------------------------------------------------- #