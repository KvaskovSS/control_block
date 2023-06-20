import json
import datetime

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file)

def load_notes():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def create_note():
    id = input("Введите идентификатор заметки: ")
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {'id': id, 'title': title, 'body': body, 'created': created}

def display_notes(notes):
    print("Список заметок:")
    for note in notes:
        print(f"Идентификатор: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Дата создания: {note['created']}")
        print("---------------------")

def filter_notes_by_date(notes):
    date_filter = input("Введите дату для фильтрации (в формате ГГГГ-ММ-ДД): ")
    filtered_notes = [note for note in notes if note['created'].startswith(date_filter)]
    display_notes(filtered_notes)

def edit_note_by_id(notes):
    note_id = input("Введите идентификатор заметки, которую хотите отредактировать: ")
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Введите новый заголовок заметки: ")
            note['body'] = input("Введите новый текст заметки: ")
            note['created'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным идентификатором не найдена.")

def delete_note_by_id(notes):
    note_id = input("Введите идентификатор заметки, которую хотите удалить: ")
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным идентификатором не найдена.")

def main():
    notes = load_notes()
    while True:
        print("1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Фильтровать заметки по дате")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выйти из приложения")

        choice = input("Введите номер операции: ")

        if choice == '1':
            note = create_note()
            notes.append(note)
            save_notes(notes)
            print("Заметка успешно создана и сохранена.")
        elif choice == '2':
            display_notes(notes)
        elif choice == '3':
            filter_notes_by_date(notes)
        elif choice == '4':
            edit_note_by_id(notes)
            save_notes(notes)
        elif choice == '5':
            delete_note_by_id(notes)
            save_notes(notes)
        elif choice == '6':
            print("Выход из приложения...")
            break
        else:
            print("Некорректный выбор операции. Попробуйте снова.")

if __name__ == '__main__':
    main()
