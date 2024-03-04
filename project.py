def shopping_program():
    final_cost = 0
    cart = []

    print('Welcome to Nike!')

    while True: 
        print('\nMenu:')
        print('1. Add this time to your cart!')
        print('2. Remove item from your cart!')
        print('3. Show cart.')
        print('4. Quit')

        choice = input('Enter your choice (1, 2, 3, 4): ')

        if choice == '1':
            name = input('Enter the item: ')
            quantity = int(input('Enter the amount of items: '))
            price = float(input('Enter price: '))
         #now were gonna put it all togrther and have a nice message
            cart.append({'name': name, 'quantity': quantity, 'price': price})
            final_cost += quantity * price 
            print('Item added to the cart!')  
        
        elif choice == '2':
            name_remover = input('What item would you like to remove: ')
            #make a name remover then use the for loop to subtract the item
            for item in cart:
                if item['name'] == name_remover:
                    final_cost -= item['quantity'] * item['price']
                    cart.remove(item)
                    print('The item had now been removed from your cart.')
                    break
            #if user doesnt put the right item namein    
            else:
                print('Item seems to not appear in your cart')
        
        elif choice == '3':
            print('\nShow Cart: ')
            for item in cart:
                #this is gonna list the the cart basicallly and then ima make it show the price
                print(f'{item['name']} - Quantity: {item['quantity']}, Price: ${item['price']:.2f}')
            print(f'Total Cost: ${final_cost:.2f}')

        elif choice == '4':
            print('\nThank you for shopping at Nike!')
            print("\nHere's your receipt!")
            for item in cart:
                print(f'{item['name']} - Quantity: {item['quantity']}, Price: ${item['price']:.2f}')
            print(f'Total Cost: ${final_cost:.2f}')
            break

        else:
            print('Invalid choice. Please enter 1, 2, 3, 4: ')

shopping_program()