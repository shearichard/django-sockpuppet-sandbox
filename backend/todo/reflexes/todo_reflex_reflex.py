from sockpuppet.reflex import Reflex


class Foobar(Reflex):
    def increment(self, step=1):
        import pprint
        print("CCCCCCCCCCCCCCCCCCCCCCC")
        pprint.pprint(self.element.dataset)
        pprint.pprint(step)
        print("RRRRRRRRRRRRRRRRRRRRRRR")
        print("WWWWWWWWWWWWWWWWW Actual increment is commented out")

class TodoReflexReflex(Reflex):
    def increment(self, step=1):
        import pprint
        print("BBBBBBBBBBBBBBBBBBBBBBB")
        pprint.pprint(self.element.dataset)
        pprint.pprint(step)
        print("YYYYYYYYYYYYYYYYYYYYYYY")
        print("WWWWWWWWWWWWWWWWW Actual increment is commented out")
        #self.count = int(self.element.dataset['count']) + step

    def indicate_that_button_has_been_pushed(self):
        print("demo A of button push has fired")

class CounterReflex(Reflex):
    def increment(self, step=10):
        import pprint
        print("AAAAAAAAAAAAAAAAAAAAAAA")
        pprint.pprint(self.element.dataset)
        pprint.pprint(step)
        print("ZZZZZZZZZZZZZZZZZZZZZZZ")
        print("XXXXXXXXXXXXXXXXX Actual increment is commented out")
        #self.count = int(self.element.dataset['count']) + step

    def indicate_that_button_has_been_pushed(self):
        print("demo B of button push has fired")
