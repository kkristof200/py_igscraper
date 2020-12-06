# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional

# Local
from .base_ig_user import BaseIGUser
from .ig_post import IGPost
from .ig_video_post import IgVideoPost
from .ig_image_post import IGImagePost
from .ig_sidecar_post import IGSidecarPost
from .enums import PostType

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ class: IgUser ------------------------------------------------------------- #

class IGUser(BaseIGUser):

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        d: dict
    ):
        super().__init__(d)

        self.bio = d['biography'].strip()
        self.bio_url = d['external_url'] if 'external_url' in d else None

        self.following_count = d['edge_follow']['count']
        self.follower_count = d['edge_followed_by']['count']

        self.is_business_account = d['is_business_account']
        self.business_category_name = d['business_category_name'] if self.is_business_account else None

        self.post_count = d['edge_owner_to_timeline_media']['count']
        self.igtv_videos_count = d['edge_felix_video_timeline']['count']

        self.related_profiles = [BaseIGUser(_d['node']) for _d in d['edge_related_profiles']['edges']]
        self.posts =  [p for p in [self.__generic_post(_d['node']) for _d in d['edge_owner_to_timeline_media']['edges']] if p]
        self.igtv_posts = [p for p in [self.__generic_post(_d['node']) for _d in d['edge_felix_video_timeline']['edges']] if p]


    # ------------------------------------------------------- Private methods -------------------------------------------------------- #

    def __generic_post(
        self,
        d: dict
    ) -> Optional[IGPost]:
        post_type = PostType(d['__typename'])

        try:
            if post_type == PostType.IMAGE:
                return IGImagePost(d)
            elif post_type == PostType.VIDEO:
                return IgVideoPost(d)
            elif post_type == PostType.SIDECAR:
                return IGSidecarPost(d)
        except Exception as e:
            print(e)

        return None


# ---------------------------------------------------------------------------------------------------------------------------------------- #