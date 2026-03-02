import pymysql
from flask import Flask, render_template, request, redirect

app = Flask("__name__")
uhost = "localhost"
uuser = "root"
upassword = ""
ucarset = "utf8mb4"
udatabase = "tugasdb"

def setup_db():
    conn = pymysql.connect(
        host=uhost,
        user=uuser,
        password=upassword,
        charset=ucarset,
        cursorclass=pymysql.cursors.Cursor
    )
    cursor = conn.cursor()
    cursor.execute("DROP DATABASE IF EXISTS tugasdb")
    cursor.execute("CREATE DATABASE tugasdb")
    cursor.execute("USE tugasdb")
    cursor.execute('''
        CREATE TABLE task (
            id INT AUTO_INCREMENT PRIMARY KEY,
            judul VARCHAR(255),
            deadline_date DATE,
            Kategori ENUM('Important', 'Urgent', 'Reguler'),
            deskripsi TEXT
        )
    ''')
    cursor.executemany('''
        INSERT INTO task (judul, deadline_date, Kategori, deskripsi)
        VALUES (%s, %s, %s, %s)
    ''', [
        ( "Belajar Flask", "2025-05-05", "Important", "Membuat API Flask dasar"),
        ( "Vue Integration", "2025-05-06", "Urgent", "Hubungkan Vue dengan Flask"),
        ( "Database Review", "2025-05-07", "Reguler", "Tinjau ERD dan relasi antar tabel"),
        ( "Uji Coba API", "2025-05-08", "Important", "Tes GET, PUT, POST endpoint"),
        ( "Burpsuite exploration", "2026-01-07", "Reguler", "Memasukan tugas BUrpsuite ke Github"),
        ( "Deploy ke Render", "2025-05-09", "Urgent", "Hosting Flask + Vue ke internet")
    ])
    conn.commit()
    cursor.close()
    conn.close()

def get_all_tasks():
    conn = pymysql.connect(
        host=uhost, user=uuser, password=upassword, database=udatabase,
        charset=ucarset, cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM task")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks

def get_by_category(category):
    print(category)
    conn = pymysql.connect(
        host=uhost, user=uuser, password=upassword, database=udatabase,
        charset=ucarset, cursorclass=pymysql.cursors.DictCursor
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM task WHERE Kategori=%s", (category,))
    task_by_category = cursor.fetchall()
    cursor.close()
    conn.close()
    return task_by_category


def create_task (title, description, deadline_date, category):
    conn = pymysql.connect(
        host=uhost, user=uuser, password=upassword, database=udatabase,
        charset=ucarset, cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO task (judul, deadline_date, Kategori, deskripsi) VALUES (%s, %s, %s, %s)",
                (title, deadline_date, category, description,))
    conn.commit()
    cursor.close()
    conn.close()
    return 

def get_task_by_id(task_id):
    conn = pymysql.connect(
        host=uhost, user=uuser, password=upassword, database=udatabase,
        charset=ucarset, cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM task WHERE id = %s", (task_id,))
    task_by_id = cursor.fetchone()
    cursor.close()
    conn.close()
    return task_by_id


def update_task(task_id, judul, deadline_date, category, description):
    conn = pymysql.connect(
        host=uhost, user=uuser, password=upassword, database=udatabase,
        charset=ucarset, cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE task SET judul = %s, deadline_date = %s, Kategori = %s, deskripsi = %s WHERE id = %s", (
            judul, deadline_date, category, description, task_id
        ))
    conn.commit()
    cursor.close()
    conn.close()
    return 


@app.route("/", methods=["GET"])
def index():
    category = request.args.get("category")
    if category:
        tasks = get_by_category(category)
    else:
        tasks = get_all_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        deadline_date = request.form["deadline_date"]
        category = request.form["category"]

        create_task(title, description, deadline_date, category)

        return redirect("/?msg=success")

    return render_template("add_task.html")

@app.route("/edit/<int:taskid>", methods=["GET", "POST"])
def edit_task(taskid):
    if request.method == "POST":
        judul = request.form["title"]
        deskripsi = request.form["description"]
        deadline_date = request.form["deadline_date"]
        Kategori = request.form["Kategori"]

        update_task(taskid, judul, deadline_date, Kategori, deskripsi)

        return redirect("/?msg=success")

    task = get_task_by_id(taskid)
    return render_template("update_task.html", task=task)



@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_task(id):
    conn = pymysql.connect(
        host=uhost,
        user=uuser,
        password=upassword,
        database=udatabase,
        charset=ucarset,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM task WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return {"status": "success", "message": "Task berhasil dihapus"}


if __name__ == "__main__":
    setup_db()
    app.run(debug=True)


