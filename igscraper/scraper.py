# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional, Union, List
import json

from kcu import request

# Pip
from ksimpleapi import Api
from kcu import strings

# Local
from .models import IGUser
from .models import IgVideoPost

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ class: Scraper ------------------------------------------------------------ #

class Scraper(Api):

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        user_agent: Optional[Union[str, List[str]]] = None,
        proxy: Optional[Union[str, List[str]]] = None,
        max_request_try_count: int = 1,
        sleep_s_between_failed_requests: Optional[float] = 0.5,
        debug: bool = False
    ):
        """init function

        Args:
            user_agent (Optional[Union[str, List[str]]], optional): User agent(s) to use for requests. If list is provided, one will be chosen randomly. Defaults to None.
            proxy (Optional[Union[str, List[str]]], optional): Proxy/Proxies to use for requests. If list is provided, one will be chosen randomly. Defaults to None.
            max_request_try_count (int, optional): How many times does a request can be tried (if fails). Defaults to 1.
            sleep_s_between_failed_requests (Optional[float], optional): How much to wait between requests when retrying. Defaults to 0.5.
            debug (bool, optional): Show debug logs. Defaults to False.
        """
        super().__init__(
            user_agent=user_agent,
            proxy=proxy,
            keep_cookies=True,
            max_request_try_count=max_request_try_count,
            sleep_s_between_failed_requests=sleep_s_between_failed_requests,
            extra_headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'},
            debug=debug
        )


    # -------------------------------------------------------- Public methods -------------------------------------------------------- #

    def get_user(
        self,
        username: str
    ) -> Optional[IGUser]:
        try:
            res = self._get('https://www.instagram.com/{}'.format(username))
            j = json.loads(strings.between(res.text, 'window._sharedData = ', '</script>').strip().rstrip(';'))

            return IGUser(j['entry_data']['ProfilePage'][0]['graphql']['user'])
        except Exception as e:
            print(e)

        return None
    
    def get_reels(
        self,
        user_id: str
    ) -> List[dict]:
        try:
            res =  self._post(
                'https://i.instagram.com/api/v1/clips/user/',
                body='target_user_id={}&page_size=12&max_id='.format(user_id).encode('utf-8'),
                extra_headers={
                    'Accept':'*/*',
                    'Origin':'https://www.instagram.com',
                    'Referer':'https://www.instagram.com/'
                }
            )

            print('res', res)
            
            return res.json()['items']
        except Exception as e:
            print(e)
        
        return None


# ---------------------------------------------------------------------------------------------------------------------------------------- #