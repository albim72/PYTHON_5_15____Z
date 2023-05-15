class PositiveTuple(tuple):
    def __new__(cls, *numbers):
        skipped_values = 0
        positive_numbers = []
        for x in numbers:
            if x>=0:
                positive_numbers.append(x)
            else:
                skipped_values+=1
        instance = super().__new__(cls,tuple(positive_numbers))
        instance.skipped_values = skipped_values
        return instance

pos_tp = PositiveTuple(0,-5,6,8,19,-3,-10,92,-22,5)
print(pos_tp)
print(type(pos_tp))
print(f'odrzucone wartości: {pos_tp.skipped_values}')
