import json
import datetime


def new_note():
    id = 1
    title = input("Введите тему заметки: ")
    msg = input("Введите текст заметки: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = {"id": id, "date": date, "title": title, "msg": msg}
    with open("notes.json", encoding="utf-8") as f:
        data = json.load(f)
        data["notes"].append(new_note)
        with open("notes.json", "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)


def add_note():
    with open("notes.json", "r", encoding="utf-8") as f:
        parse = json.loads(f.read())
        lst = []
        for txt in parse["notes"]:
            lst.append(txt["id"])
            id = lst[-1]+1
    title = input("Введите заголовок: ")
    msg = input("Введите текст заметки: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    new_note ={"id": id, "date": date, "title": title, "msg": msg}
    with open("notes.json", encoding="utf-8") as f:
        data = json.load(f)
        data["notes"].append(new_note)
        with open("notes.json", "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)


def read_note():
    with open("notes.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
        for txt in data["notes"]:
            print(f'{txt["id"]: > 3}. Заголовок: {txt["title"]+"   "} Текст заметки: {txt["msg"]+"   "} {txt["date"]}')
            print("-"*130)


def remove_note():
    id_for_del = int(input("Выберите какую заметку удалить: "))
    with open("notes.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        minimal = 0
        for txt in data["notes"]:
            if txt["id"] == id_for_del:
                data["notes"].pop(minimal)
            else:
                None
            minimal = minimal + 1
        with open("notes.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)


def edit_note():
    id_for_del = int(input("Выберите какую заметку редактировать: "))
    with open("notes.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        minimal = 0
        for txt in data["notes"]:
            if txt["id"] == id_for_del:
                txt["title"] = input("Измените заголовок заметки: ")
                txt["msg"] = input("Измените текст заметки: ")
                txt["date"] = datetime.datetime.now().strftime("%Y-%m-%d")
        with open("notes.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)


def date_selection():
    date_for_selection = input("Введите дату для просмотра заметки: ")
    with open("notes.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for txt in data["notes"]:
            if txt["date"] == date_for_selection:
                print(f'{txt["id"]: > 3}. Заголовок: {txt["title"]+"   "} Текст заметки: {txt["msg"]+"   "} {txt["date"]}')
                print("-" * 100)


def menu():
    menu_points=[
        "Создать заметку",
        "Добавить заметку",
        "Редактировать заметку",
        "Удалить заметку",
        "Показать весь список заметок",
        "Показать список заметок определенной даты",
        "Выход"
    ]
    print('Главное меню')
    [print(f'\t{i}. {item}') for i, item in enumerate(menu_points, 1)]
    choise = int(input('Выберите пункт меню: '))
    return choise


while True:
    choise = menu()
    match choise:
        case 1:
            new_note()
            print("\nФайл успешно создан!\n")
        case 2:
            add_note()
            print("\nЗаметка успешно добавлена!\n")
            read_note()
        case 3:
            read_note()
            edit_note()
            print("\nЗаметка успешно отредактирована!\n")
            read_note()
        case 4:
            remove_note()
            print("\nЗаметка успешно удалена!\n")
            read_note()
        case 5:
            read_note()
        case 6:
            read_note()
            date_selection()
        case 7:
            print('\nВсего хорошего!')
            break
