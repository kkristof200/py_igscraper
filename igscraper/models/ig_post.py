# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
import time

# Pip
from jsoncodable import JSONCodable

# Local
from .enums import PostType
from .size import Size
from .core_ig_user_data import CoreIGUserData
from .base_ig_post import BaseIGPost

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ class: IgPost ------------------------------------------------------------- #

class IGPost(BaseIGPost):

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        d: dict
    ):
        super().__init__(d)

        self.thumbnail_src = d['thumbnail_src']
        self.caption = d['edge_media_to_caption']['edges'][0]['node']['text'] if d['edge_media_to_caption']['edges'] else None

        self.like_count = d['edge_liked_by']['count']
        self.comment_count = d['edge_media_to_comment']['count']
        self.timestamp = d['taken_at_timestamp']


    # ------------------------------------------------------ Public properties ------------------------------------------------------- #

    @property
    def age_seconds(self) -> float:
        return time.time() - self.timestamp


    # -------------------------------------------------------- Public methods -------------------------------------------------------- #



    # ------------------------------------------------------ Private properties ------------------------------------------------------ #



    # ------------------------------------------------------- Private methods -------------------------------------------------------- #




# ---------------------------------------------------------------------------------------------------------------------------------------- #