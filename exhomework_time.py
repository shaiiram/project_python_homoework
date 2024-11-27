#! /usr/bin/env python3
class Time:
    def __init__(self, A, B):
        if A is None or B is None:
            raise ValueError(f'Both hours {A} and minutes {B} must be defined.')
        if not (0 <= A <= 12):
            raise ValueError("Hours (A) must be between 0 and 12.")
        if not (0 <= B <= 59):
            raise ValueError("Minutes (B) must be between 0 and 59.")
        self.A = A
        self.B = B

    def __str__(self):
        return f"{self.A:02}:{self.B:02}"

    def __add__(self, other):
        total_minutes = self.B + other.B
        extra_hours = total_minutes // 60
        remaining_minutes = total_minutes % 60
        total_hours = self.A + other.A + extra_hours
        wrapped_hours = total_hours % 12
        return Time(wrapped_hours, remaining_minutes)

    def __repr__(self):

        return f"Time(hours={self.A}, minutes={self.B})"

    def __eq__(self, other):
        if isinstance(other, Time):
            return self.A == other.A and self.B == other.B
        return False


def main():
    A = None
    B = None
    time1 = None
    time2 = None

    while True:
        print('''
        (A): choose hours, and minutes
        (B): Add time to existing time
        (R): Repr
        (E) equal
        (T) The time your chose of A 
        (Q) quit
          ''')

        option = input('option: '.upper())

        match option:
            case 'A':
                try:
                    A = int(input('enter hours'))
                    B = int(input('enter minutes'))
                    time1 = Time(A, B)
                    if not (0 <= A <= 12):
                        print("Hours must be between 0 and 12.")
                    if not (0 <= B <= 59):
                        print('minutes must be between 0-59')

                except ValueError:
                    print('this is not hour only number pls!')

            case 'T':
                if A is not None and B is not None:
                    print(f"Both hours and minutes are defined: {A:02}:{B:02}")
                else:
                    print("Please define both hours and minutes before continuing.")

            case 'B':
                if A is not None and B is not None:
                    time1 = Time(A, B)
                    print("Enter additional time:")
                    try:
                        new_hours = int(input('enter a hours'))
                        new_minutes = int(input('enter a minutes'))
                        time2 = Time(new_hours, new_minutes)
                        print(f"Time 1: {time1}, Time 2: {time2}")
                    except ValueError:
                        print('Invalid input for hours or minutes.')
                    else:
                        time3 = time1 + time2
                        print(f'The sum of times is {time3}\n')
                        print(f'The repr of times is {repr(time3)}')
            case 'R':
                if A is not None and B is not None:
                    time1 = Time(A, B)
                    print(f"The defined time is: {repr(time1)}")
                else:
                    print("Please define both hours and minutes before continuing.")
            case 'E':
                if time1 is None or time2 is None:
                    print("You must define both time1 and time2 before using this option.")
                else:
                    if time1 == time2:
                        print("The times are equal!")
                    else:
                        print("The times are not equal.")

            case 'Q':
                break


if __name__ == "__main__":
    main()
