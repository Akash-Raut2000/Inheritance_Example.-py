class Parent:
    def greet (self):
        return f"Hello from Akash"

class Child(Parent):
    pass

child=Child()
print(child.greet())