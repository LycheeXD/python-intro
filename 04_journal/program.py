import journal


def main():
    print_header()
    process_user_input()


def print_header():
    print('------------------------')
    print('         journal')
    print('------------------------')


def process_user_input():
    print('what you wanna do? ')

    journal_name = 'name'
    journal_entries = journal.load_journal(journal_name)

    print('imported journal', journal_entries)

    user_command = None
    # journal_entries = []

    while user_command != 'x':
        user_command = input('[L]ist, [A]dd, e[X]it: ').lower().strip()

        if user_command == 'l':
            list_entries(journal_entries)
        elif user_command == 'a':
            add_entry(journal_entries)
        elif user_command != 'x':
            print('invalid input')

    journal.save_journal(journal_name, journal_entries)

    print('bye')


def list_entries(journal_entry_list):
    reversed_journal_entry_list = reversed(journal_entry_list)

    for index, each_entry in enumerate(reversed_journal_entry_list):
        print('[{}] {}'.format(index + 1, each_entry))


def add_entry(journal_entry_list):
    new_entry = input('add entry: ')

    # journal_entry_list.append(new_entry)
    journal.add_journal_entry(new_entry, journal_entry_list)


if __name__ == '__main__':
    main()
