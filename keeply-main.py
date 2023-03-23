import sqlite3
conexao = sqlite3.connect('keeply-db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE if not exists CATEGORY (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (50)
);''')
               
cursor.execute('''CREATE TABLE if not exists TASK (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (50) UNIQUE,
    date VARCHAR (10),
    status VARCHAR (10),
    category_id INT NOT NULL,
        FOREIGN KEY (category_id) REFERENCES category(id)
);''')
               

def main_menu():
    print('-' * 30)
    print('-=-= TASKS =-=-')
    print('1 - Create task\n2 - Update task\n3 - Delete task\n4 - List tasks\n5 - Check task')
    print('-' * 30)
    print('-=-= CATEGORIES =-=-')
    print('6 - Create category\n7 - Update category\n8 - Delete category\n9 - List all categories')
    print('-' * 30)


def insert_task():
    TaskName = str(input('Task name: ')).strip()
    TaskDate = str(input('Task date (mm/dd/yyyy): ')).strip()
    TaskStatus = str(input('Task status: ')).strip()
    TaskCateg = str(input('Task category: ')).strip()
    data = [TaskName, TaskDate, TaskStatus, TaskCateg]
    sql_insert_task = 'insert into TASK(name, date, status, category_id) VALUES (?, ?, ?, ?)'
    cursor.execute(sql_insert_task, data)
    conexao.commit()
    print(f'| {TaskName} | {TaskDate} | {TaskStatus} | {TaskCateg} | OK!' )


def update_task():
    UpTask = str(input('Task name to be updated: ')).strip()
    UpTaskName = str(input('New task name: ')).strip()
    UpTaskDate = str(input('New task date: ')).strip()
    UpTaskStatus = str(input('New task status: ')).strip()
    UpTaskCateg = str(input('New task category: ')).strip()
    data = [UpTaskName, UpTaskDate, UpTaskStatus, UpTaskCateg, UpTask]
    sql_up_task = 'UPDATE TASK SET name = ?, date = ?, status = ?, category_id = ? WHERE name = ?'
    cursor.execute(sql_up_task, data)
    conexao.commit()
    print(f'| {UpTaskName} | {UpTaskDate} | {UpTaskStatus} | {UpTaskCateg} | OK!')    


def delete_task():
    DelTask = str(input('Task name to be deleted: ')).strip()
    data = [DelTask]
    sql_del_task = 'DELETE from TASK WHERE name = ?'
    cursor.execute(sql_del_task, data)
    conexao.commit()
    print('Deleted!')


def select_all_tasks():
        sql_sel_all_tasks = '''SELECT * from TASK'''
        SelAllTasks = cursor.execute(sql_sel_all_tasks)
        for task in SelAllTasks:
            print(task)


def select_bydate_tasks():
    SelTaskByDate = str(input('Date [dd/mm/yyyy]: ')).strip()
    data = [SelTaskByDate]
    sql_sel_task_date = 'SELECT * from TASK WHERE date = ?'
    SelTaskDate = cursor.execute(sql_sel_task_date, data)
    for task in SelTaskDate:
        print(task)


def check_task():
    CheckedTask = str(input('Task name to be checked: ')).strip()
    data = ['CHECKED', CheckedTask]
    sql_check_task = 'UPDATE TASK SET status = ? WHERE name = ?'
    CheckTask = cursor.execute(sql_check_task, data)
    conexao.commit()
    print('Checked!') 


def insert_category():
    NewCateg = str(input('New category name: ')).strip()
    data = [NewCateg]
    sql_new_categ = 'INSERT into CATEGORY (name) VALUES (?)'
    InsertCateg = cursor.execute(sql_new_categ, data)
    conexao.commit()
    print('New category added!')


def update_category():
    OldCateg = str(input('Category name to be updated: ')).strip()
    NewCateg = str(input('New category name: ')).strip()
    data = [NewCateg, OldCateg]
    sql_up_categ = 'UPDATE CATEGORY SET name = ? WHERE name = ?'
    UpCateg = cursor.execute(sql_up_categ, data)
    conexao.commit()
    print('Category updated!')


def delete_category():
    DelCateg = str(input('Category name to be deleted: ')).strip()
    data = [DelCateg]
    sql_del_categ = 'DELETE from CATEGORY WHERE name = ?'
    DeleteCateg = cursor.execute(sql_del_categ, data)
    conexao.commit()
    print('Category deleted!')


def select_all_categories():
    sql_sel_all_categ = 'SELECT * FROM CATEGORY'
    SelAllCateg = cursor.execute(sql_sel_all_categ)
    conexao.commit()
    for categ in SelAllCateg:
        print(categ)

###########

main_menu()
Opt = int(input('Choose your option: '))
 
while True:
    if Opt > 10:
        while True:
            Opt = int(input('Invalid option! Try again: '))
            if Opt < 10:
                break     
    elif Opt == 1:
        insert_task()
    elif Opt == 2:
        update_task()
    elif Opt == 3:
        delete_task()
    elif Opt == 4:
        print('1 - List all tasks\n2 - List by date')
        OptTasks = int(input('Choose option: '))
        if OptTasks == 1:
            select_all_tasks()
        elif OptTasks == 2:
            select_bydate_tasks()
    elif Opt == 5:
        check_task()
    elif Opt == 6:
        insert_category()
    elif Opt == 7:
        update_category()
    elif Opt == 8:
        delete_category()
    elif Opt == 9:
        select_all_categories()

    opt_continue = str(input('Do you wish to continue? [Yes/No] ')).strip().lower()
    if opt_continue not in 'yesno':
        while True:
            opt_continue = str(input('Invalid option!\nDo you wish to continue? [Yes/No] ')).strip().lower()
            if opt_continue in 'yesno':
                break
    if opt_continue in 'yes':
        main_menu()
        Opt = int(input('Choose your option: '))
    elif opt_continue in 'no':
        print('See you later!')
        break
        


conexao.commit()
conexao.close
