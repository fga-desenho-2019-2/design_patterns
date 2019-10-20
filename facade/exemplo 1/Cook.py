from Cutter import Cutter
from Boiler import Boiler
from Frier import Frier


class Cook(object):

    def cut(self, item):
        cutter = Cutter(item)
        cutter.cutItem()

    def boil(self, item):
        boiler = Boiler(item)
        boiler.boilItem()

    def fry(self, item):
        frier = Frier(item)
        frier.fryItem()

    def prepareDish(self, item):
        self.cut(item)
        self.boil(item)
        self.fry(item)
