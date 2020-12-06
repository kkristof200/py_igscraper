from igscraper import *
from randomua import RandomUA

scraper = Scraper(user_agent=RandomUA.firefox(min_browser_version=70), debug=True)
user = scraper.get_user('pubity')
# user.save('test.json')

all_users = [user.related_profiles]

for _user in user.related_profiles:
    try:
        all_users.extend(scraper.get_user(_user.username).related_profiles)
    except Exception as e:
        print(_user.username, e)



from kcu import kjson

kjson.save(all_users, 'test.json')

# print(scraper.get_reels(user.id))