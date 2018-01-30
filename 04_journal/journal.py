import os


def get_full_file_name(journal_name):
    return os.path.abspath(os.path.join('.', 'journals', journal_name + '.jrl'))


def load_journal(journal_name):
    """
    creates and loads new journal

    :param journal_name: name of the journal to load
    :return: journal data populated with file data
    """
    journal_data = []

    file_name = get_full_file_name(journal_name)

    if os.path.exists(file_name):
        with open(file_name) as fin: # fin: file input
            for entry in fin.readlines():
                journal_data.append(entry.rstrip())
                print('journal load ' + entry.rstrip())

    return journal_data


def save_journal(journal_name, journal_data):
    # file_name = './journals' + journal_name

    file_name = get_full_file_name(journal_name)

    print('saving to {}'.format(file_name))

    # fout: file output
    # fout = open(file_name, 'w')
    with open(file_name, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')

    # fout.close()


def add_journal_entry(journal_name, journal_data):
    journal_data.append(journal_name)
