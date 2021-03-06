# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# Local
from .ig_post import IGPost

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------------------- class: IgImagePost ---------------------------------------------------------- #

class IGImagePost(IGPost):

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        d: dict
    ):
        super().__init__(d)

        self.image_url = self.display_url


# ---------------------------------------------------------------------------------------------------------------------------------------- #