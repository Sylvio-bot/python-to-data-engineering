class Fraction:
    def __init__(self, num:int, denom:int):
        if denom == 0:
            raise ValueError("Denominator cannot be zero")

        self.num = num
        self.denom = denom

    def __str__(self):
        return f'{self.num} / {self.denom}'

    def __mul__(self, other):
        top = self.num * other.num
        bottom = self.denom * other.denom
        return Fraction(top , bottom)


def main():
    frac_1 = Fraction(1, 0)
    frac_2 = Fraction(2, 4)

    frac_3 = frac_1 * frac_2
    print(f"{frac_1} times {frac_2} equal {frac_3}")

 
if __name__ == "__main__":
    main()
