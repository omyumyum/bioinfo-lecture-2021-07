
d_persons = {'Guillaume':'Canada', 'Niklas':'Germany', 'Mark':'USA', 'Alex':'Swiss', 'Alberto':'Italia'}

class Person:
    nation = ''
    
    def showNation(self):
        print(self.nation)
    def setNation(self, whichNation):
        self.nation = whichNation

Guillaume = Person()
Guillaume.setNation(d_persons['Guillaume'])
Guillaume.showNation()

Niklas = Person()
Niklas.setNation(d_persons['Niklas'])
Niklas.showNation()

Mark = Person()
Mark.setNation(d_persons['Mark'])
Mark.showNation()

Alex = Person()
Alex.setNation(d_persons['Alex'])
Alex.showNation()

Alberto = Person()
Alberto.setNation(d_persons['Alberto'])
Alberto.showNation()
