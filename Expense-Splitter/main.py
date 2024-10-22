def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    if number_of_people <= 1:
        raise ValueError("Number of people must be greater than 1.")

    share_per_person: float = total_amount / number_of_people

    print(f'total expenses: {currency}{total_amount}')
    print(f'number of people: {number_of_people}')
    print(f"Share per person: {currency}{share_per_person:.2f}")


def main() -> None:
    try:
        total_amount: float = float(input("Enter total amount to be split: "))
        number_of_people: int = int(input("Enter number of people to be split: "))
        currency: str = str(input("Enter currency to split the amount: ")).upper()

        calculate_split(total_amount, number_of_people, currency)
    except ValueError as e:
        print(e)
    
    
if __name__ == '__main__':
    main()