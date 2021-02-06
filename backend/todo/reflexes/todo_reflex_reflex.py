from sockpuppet.reflex import Reflex


class TodoReflexReflex(Reflex):
    def increment(self, step=1):
        self.count = int(self.element.dataset['count']) + step
    def indicate_that_button_has_been_pushed(self):
        print("demoofbuttonpush has fired")
