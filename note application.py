note_list = []

def note():
    print("""
 ******************************************
    Menu
    1. Create note
    2. View note
    3. Update note
    4. Delete note
    5. Exit
 ******************************************
    """)
    choice = eval (input("Enter the number of your choice: "))

    if choice == 1:
        title = input("[TITLE] What do you want to name your file/note? ")
        user_note = input('\n[CONTENT] Write your note here: ')
        note_list.append([title, user_note])
        print("Note Saved Successfully!")


    elif choice == 2:
        if len(note_list) > 0:
            for i in range(len(note_list)):
                print(f"""
{i + 1}. Title: {note_list[i][0]}
Content: 
{note_list[i][1]}""")
        else:
            print('No notes written yet!')


    elif choice == 3:
        if len(note_list) > 0:
            for i in range(len(note_list)):
                print(f"""
{i + 1}. Title: {note_list[i][0]}
Content: 
{note_list[i][1]}""")
            user_choice = int(input('\nWrite the number you want to update: '))
            if user_choice <= len(note_list) and user_choice > 0:
                updated_user_note = input('\nWrite your updated note here: ')
                note_list[user_choice - 1][1] = updated_user_note
                print("Note Updated Successfully!")
            else:
                print('Invalid choice. Please select a valid note to update.')
        else:
            print('No notes written yet!')


    elif choice == 4:
        if len(note_list) > 0:
            for i in range(len(note_list)):
                print(f"""
{i + 1}. Title: {note_list[i][0]}
Content: 
{note_list[i][1]}""")
            user_choice = int(input('\nWrite the number you want to delete: '))
            if user_choice <= len(note_list) and user_choice > 0:
                note_list.remove(note_list[user_choice - 1])
                print("Note Deleted Successfully!")
            else:
                print('Invalid choice. Please select a valid note to delete.')
        else:
            print('No notes written yet!')


    elif choice == 5:
        print('Thank You For Using Our Note App!')
        quit()

    else:
        print('Invalid choice. Please select a valid option.')
        

while True:
    note()
    quitt = input('Do you want to continue (Y/N): ').upper()

    if quitt == 'Y':
        note()

    elif quitt == 'N':
            print('Thank You For Using Our Note App!')
            break

    else:
        print('Invalid choice. Please enter Y or N.')
