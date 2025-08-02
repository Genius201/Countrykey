#Carl Shaffer CIS261 Country Key
def display_menu():
    print('--- Country Key Database Menu ---')
    print('Command Menu:')
    print('view - View a country')
    print('add - Add a country')
    print('del - Delete a country')
    print('exit - Exit the program')
    print('----------------------------------')


def prepopulate_countries():
    return {
      "USA": "United States of America",
      "CAN": "Canada",
      "MEX": "Mexico",
    }
    

def view_country(countries):
    print('\nAvailable Countries (keys):')
    for key in countries:
        print(f' -{key}')
    key_to_view = input('Enter the key for the country you want to view:').upper()
    if key_to_view in countries:
       print(f'\nCountry:{countries[key_to_view]}')
    else:
       print('\nInvalid key. Please try again')

def add_country(countries):
    new_key = input('Enter the key for the new country (e.g.,FRA):').upper()
    if new_key in countries:
       print(f'\nError: The key "{new_key}" already exists.')
    else:
       new_name = input("Enter the new country name: ")
       countries[new_key] = new_name
       print(f'\nSuccess! "{new_name}" has been added.')

def delete_country(countries):
    key_to_delete = input('Enter the key of the country to delete: ').upper()
    if key_to_delete in countries:
        del countries[key_to_delete]
        print(f'\nSuccess! The country with key "{key_to_delete}" has been deleted.')
    else:
        print(f"\nError: The key '{key_to_delete}' does not exist.")

def main():
  countries = prepopulate_countries()
  running = True

  while running:
   print()
   display_menu()
   command = input('Enter a command: ').lower()
   if command == 'view':
      view_country(countries)
   elif command == 'add':
      add_country(countries)
   elif command == 'del':
      delete_country(countries)
   elif command == 'exit':
      running = False
      print('Exiting program. Goodbye!')
   else:
      print('\nInvalid command. Please choose from command menu.')

if __name__ == "__main__":
   main()
