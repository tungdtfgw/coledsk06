def auto_vending():
    while True:
        print_menu()
        choice = get_choice()
        payment(choice)

def print_menu():
    print('--- Vending Machine Menu ---')
    print('1. Aqua ($1.5)')
    print('2. Coke ($2)')
    print('3. Orange ($3.99)')

def get_choice():
    choice = int(input('Your choice: '))
    if 0 < choice < 4:
        return choice
    return 0

def payment(choice):
    if choice == 0:
        print('Invalid choice. Please try again.')
        return
    
    if choice == 1:
        payment = 1.5
    elif choice == 2:
        payment = 2
    else:
        payment = 3.99

    print(f'Payment: ${payment:.2f}. Thank you for your purchase!')

if __name__ == '__main__':
    auto_vending()