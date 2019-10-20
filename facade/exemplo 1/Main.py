from Cook import Cook

class Main(object):

    if __name__ == "__main__":
        cook = Cook()

        cook.cut('carrot')
        cook.boil('carrot')
        cook.fry('carrot')

        cook.prepareDish('broccoli')