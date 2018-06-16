class Parent(oject):
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad =Parent()
son =Child()

dad.implicit()
son.implicit()

