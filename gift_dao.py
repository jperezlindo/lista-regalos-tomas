import json, os

class GiftDAO():
    __PATH_GIFTED = os.path.dirname(__file__) + '/gifted.json'
    __PATH_GIFTS = os.path.dirname(__file__) + '/gifts.json'

    @classmethod
    def get_gifts(cls):
        try:
            with open(cls.__PATH_GIFTS, 'r', encoding='utf8') as ungift:
                gifts = json.load(ungift)
                return gifts
        except Exception as e:
            print(e)

    @classmethod
    def get_gifted(cls):
        try:
            with open(cls.__PATH_GIFTED, 'r', encoding='utf8') as gift:
                gifted = json.load(gift)
                return gifted
        except Exception as e:
            print(e)

    @classmethod
    def store_gifts(cls, gifts):
        try:
            with open(cls.__PATH_GIFTS, 'w', encoding='utf8') as ungift:
                json.dump(gifts, ungift, indent=4)
        except Exception as e:
            print(e)

    @classmethod
    def store_gifted(cls, gifted):
        try:
            with open(cls.__PATH_GIFTED, 'w', encoding='utf8') as gifts:
                json.dump(gifted, gifts, indent=4)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    GiftDAO.get_gifts()
