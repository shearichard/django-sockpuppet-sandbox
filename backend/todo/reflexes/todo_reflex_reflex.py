from sockpuppet.reflex import Reflex


class TodoReflexReflex(Reflex):
    def increment(self, step=1):
        self.count = int(self.element.dataset['count']) + step
