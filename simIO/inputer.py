
def SetupInputer(theInputer):
    global inputer
    inputer = theInputer
    print("Setting up global inputer")

class Inputer:
    def __init__(self):
        self.sources = []
    def addSource(self, newSource):
        print("Attaching a "+newSource.title)
        self.sources.append(newSource)
    def send(self, event):
        for source in self.sources:
            source.send(event)
