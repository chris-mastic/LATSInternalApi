class AssessOrdersDTO:
    # Initialize assessValues as a list with a default empty dictionary
    def __init__(self):
        self._ltc_sub_class_old = None
        self._ltc_sub_class_new = None
        self._quantity_old = None
        self._quantity_new = None
        self._units_old = None
        self._units_new = None
        self._other_exempt_old = None
        self._other_exempt_new = None
        self._value_old_total = None 
        self._value_new_total = None 
        self._value_old_hs = None 
        self._value_new_hs = None 
        self._value_old_tp = None 
        self._value_new_tp = None 

        # Getter method (property)
        @property
        def ltc_sub_class_old(self):
            return self._ltc_sub_class_old

        # Setter method (setter)
        @ltc_sub_class_old.setter
        def ltc_sub_class_new(self,value):
            if value < 0:
                raise ValueError("Whatever")
            self._ltc_sub_class_old = value

        @property
        def ltc_sub_class_new(self):
            return self._ltc_sub_class_new

        # Setter method (setter)
        @ltc_sub_class_new.setter
        def ltc_sub_class_new(self,value):
            if value < 0:
                raise ValueError("Whatever")
            self._ltc_sub_class_new = value

        @property
        def quantity_old(self):
            return self._quantity_old

        # Setter method (setter)
        @quantity_old.setter
        def ltc_sub_class_old(self,value):
            if value < 0:
                raise ValueError("Whatever")
            self._quantity_old = value

        @property
        def quantity_new(self):
            return self._quantity_new
        # Setter method (setter)
        @quantity_new.setter
        def quantity_new(self,value):
            if value < 0:
                raise ValueError("Whatever")
            self._quantity_new = value

        @property
        def units_old(self):
            return self._units_old

        # Setter method (setter)
        @units_old.setter
        def units_old(self,value):
            if value < 0:
                raise ValueError("Whatever")
            self._units_old = value

        @property
        def units_new(self):
            return self._units_new

        # Setter method (setter)
        @units_new.setter
        def units_new(self,value):
            if value < 0:
                raise ValueError("Whatever")
            self._units_new = value

        @property
        def other_exempt_old(self):
            return self._other_exempt_old

        # Setter method (setter)
        @other_exempt_old.setter
        def other_exempt_old(self,value):
            if value < 0:
                raise ValueError("Whatever")
            self._other_exempt_old = value

        @property
        def other_exempt_new(self):
            return self._other_exempt_new

        # Setter method (setter)
        @other_exempt_new.setter
        def other_exempt_new(self,value):
            if value < 0:
                raise ValueError("Whatever")
            self._other_exempt_new = value

        @property
        def value_old_total(self):
            return self._value_old_total

        # Setter method (setter)
        @value_old_total.setter
        def value_old_total(self,value):
            if value < 0:
                raise ValueError("Whatever")
            self._value_old_total = value

        @property
        def value_new_total(self):
            return self._value_new_total

        # Setter method (setter)
        @value_new_total.setter
        def value_new_total(self,value):
            if value < 0:
                raise ValueError("Whatever")
            self._value_new_total = value

        @property
        def value_old_hs(self):
            return self._value_old_hs

        # Setter method (setter)
        @value_old_hs.setter
        def value_old_hs(self,value):
            if value < 0:
                raise ValueError("Whatever")
            self._value_old_hs = value

        @property
        def value_new_hs(self):
            return self._value_new_hs

        # Setter method (setter)
        @value_new_hs.setter
        def value_new_hs(self,value):
            if value < 0:
                raise ValueError("Whatever")
            self._value_new_hs= value

        @property
        def value_old_tp(self):
            return self._value_old_tp

        # Setter method (setter)
        @value_old_tp.setter
        def value_old_tp(self,value):
            if value < 0:
                raise ValueError("Whatever")
            self._value_old_tp= value

        @property
        def value_new_tp(self):
            return self._value_new_tp

        # Setter method (setter)
        @value_new_tp.setter
        def value_new_tp(self,value):
            if value < 0:
                raise ValueError("Whatever")
            self._value_new_tp = value




# EXAMPLE
            
# class MyClass:
#     def __init__(self):
#         self._my_attribute = None  # Initialize the attribute (with an underscore for convention)

#     # Getter method (property)
#     @property
#     def my_attribute(self):
#         return self._my_attribute

#     # Setter method (setter)
#     @my_attribute.setter
#     def my_attribute(self, value):
#         # You can add validation or other logic here
#         if value < 0:
#             raise ValueError("Attribute value must be non-negative")
#         self._my_attribute = value

# Example usage

# obj = MyClass()

# # Set the attribute using the setter
# obj.my_attribute = 42

# # Get the attribute using the getter
# print(f"My attribute value: {obj.my_attribute}")