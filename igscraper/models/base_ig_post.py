# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# Pip
from jsoncodable import JSONCodable

# Local
from .enums import PostType
from .size import Size
from .core_ig_user_data import CoreIGUserData

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------------------- class: BaseIGPost ----------------------------------------------------------- #

class BaseIGPost(JSONCodable):

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        d: dict
    ):
        self.type = PostType(d['__typename'])
        self.id = d['id']
        self.shortcode = d['shortcode']
        self.url = 'https://www.instagram.com/p/{}'.format(self.shortcode)

        self.size = Size(d['dimensions'])
        self.display_url = d['display_url']

        self.is_video = d['is_video']

        self.owner = CoreIGUserData(d['owner'])


# ---------------------------------------------------------------------------------------------------------------------------------------- #