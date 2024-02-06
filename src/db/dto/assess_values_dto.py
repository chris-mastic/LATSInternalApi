class AssessOrdersDTO:
    # Initialize assessValues as a list with a default empty dictionary
    def __init__(self, ltc_sub_class_old, ltc_sub_class_new, quantity_old, quantity_new,
                 units_old, units_new, other_exempt_old, other_exempt_new, value_old_total,
                 value_new_total, value_old_hs, value_new_hs, value_old_tp, value_new_tp):
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

        @ltc_sub_class_old.setter
        def ltc_sub_class_old(self,value):
            if value < 0:
                raise ValueError("Whatever")
            self._ltc_sub_class_old = value


# obj = MyClass()

# # Set the attribute using the setter
# obj.my_attribute = 42

# # Get the attribute using the getter
# print(f"My attribute value: {obj.my_attribute}")