# Instance, static and class methods

class MyClass:

    # Regular instance method.
    # Through the self parameter, instance methods can freely access attributes and other methods on the same object.
    # Not only can they modify object state, instance methods can also access the class itself through the
    # self.__class__ attribute. This means instance methods can also modify class state.
    def method(self):
        return 'Instance method called', self

    # Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the
    # object instance—when the method is called
    @classmethod
    def classmethod(cls):
        return 'Class method called', cls

    # This type of method takes neither a self nor a cls parameter. Therefore a static method can neither modify
    # object state nor class state.
    @staticmethod
    def staticmethod():
        return 'Static method called'


# Calling the methods with an instance:
obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())
print()
# Calling the methods without an instance:
# print(MyClass.method())  # This would not work because an instance method requires an instance of that class
print(MyClass.classmethod())
print(MyClass.staticmethod())
