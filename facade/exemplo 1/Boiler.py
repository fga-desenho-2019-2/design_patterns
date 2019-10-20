class Boiler(object):

    def __init__(self, item):
        self.boilingItem = item

    def boilItem(self):
        print(self.boilingItem + ' has been boiled' )