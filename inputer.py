import threading

class Inputer:
    def __init__(self):
        self.controllers = []
    def addController(self, newController):
        print("Attaching input controller")
        self.controllers.append(newController)
    def send(self, event):
        for controller in self.controllers:
            controller.send(event)
