from gift_dao import GiftDAO

class Gift:

    @classmethod
    def delete_gift(cls, id):
        gifts = GiftDAO.get_gifts()
        if gifts is not None:
            for gift in gifts['list']:
                if gift['id'] == int(id):
                    if gift['cant'] == 1:
                        gifts['list'].remove(gift)
                        break
                    else:
                        gift['cant'] -= 1
                        break
        return gifts, gift
    
    @classmethod
    def set_to_gifted(cls, present):
        not_in_list = True
        gifted = GiftDAO.get_gifted()
        if gifted is not None:
            for gift in gifted['list']:
                if gift['id'] == present['id']:
                    gift['cant'] += 1
                    if present['who'] != '':
                        gift['who'].append(present['who'][0])
                    not_in_list = False
                    break
            if not_in_list:
                present['cant'] = 1
                gifted['list'].append(present)

        return gifted

