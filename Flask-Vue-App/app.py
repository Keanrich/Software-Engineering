from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

def initialize_db():
    conn =  pymysql.connect(
        host='localhost',
        password='',
        user='root',
        charset='utf8mb4'
    )
    
    cursor = conn.cursor()
    cursor.execute('create database if not exists CVsitedb')
    cursor.execute('use CVsitedb')
    cursor.execute(''' 
        create table if not exists user_CV(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nama VARCHAR(255),
        password VARCHAR(255)
        )
            ''')
    
    cursor.execute('''
        create table if not exists photo_CV (
        pid INT AUTO_INCREMENT PRIMARY KEY,
        uid INT,  
        foto TEXT,
        FOREIGN KEY (UID) REFERENCES user_CV(id)
        )
            ''')
    
    cursor.execute('''
        create table if not exists  isi_CV(
        iid INT AUTO_INCREMENT PRIMARY KEY,
        uid INT,
        kategori ENUM('Proyek', 'KerjaOrganisasi', 'Perkenalan', 'Lainnya'),
        isi TEXT
                )
            ''')
    
    conn.commit()
    cursor.close()
    conn.close()

def insert_db():
    conn =  pymysql.connect(
        host='localhost',
        password='',
        user='root',
        charset='utf8mb4',
        database='CVsitedb'
    )
    
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO user_CV (nama, password)
        VALUES (%s, %s)
        ''', [
            ('Keanrich', 'ken230925'), 
            ('Stefani', 'stef230526'), 
            ('Steven', 'sutrisno123'), 
            ('Manuel', 'gellen321'),
            ('Reuben', 'Ryu345')
            ])
    
    cursor.executemany(
        '''
        INSERT INTO photo_CV (uid, foto)
        VALUES (%s, %s)
        ''', [
            (0, 'inti_ken.jpg'), (0, 'l_ken.jpg'), (0, 'r_ken.jpg'),
            (1, 'inti_stef.jpg'), (1, 'l_stef.jpg'), (1, 'r_stef.jpg')
            ])
    
    cursor.executemany(
        '''
        INSERT INTO isi_CV (uid, kategori, isi)
        VALUES (%s, %s, %s)
        ''', [
            (0, 'Perkenalan', 'Nama: Keanrich Cordana, Program Studi: IBDA 2023, Umur: 19 Tahun, Tempat Tanggal Lahir: Pangkalan Bun 23 Mei 2006, Hobi: Programming; Main Game; Baca Buku; GYM'),
            (0, 'KerjaOrganisasi', 'BEM Calvin Institute of Technology 2024/2025, Student Employment Program Web Designer, Student Employment Program Lecturer Assistant, Web Developer Yayasan Lembaga SABDA'),
            (1, 'Perkenalan', 'Stefani Tania, BMS 2023, 20 Tahun, Jakarta, 23 September 2005'),
            (0, "Proyek", "Pengembangan Situs Drupal Reformed Yayasan Lembaga SABDA, Membuat Situs CV dengan Vue JS + Python + Tailwind, Perpustakaan Mini menggunakan Python + Tkinter, Sistem CarRental Python + HTML + CSS, Sistem Ecommerce Oriented Programming")
        ]
    )

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    name = data.get('username')
    password = data.get('password')
    
    conn =  pymysql.connect(
        host='localhost',
        password='',
        user='root',
        charset='utf8mb4',
        database='CVsitedb',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try:
        cursor = conn.cursor()
        sql = "SELECT id, nama, password from user_CV where nama=%s and password=%s"
        cursor.execute(sql, (name, password))
        user = cursor.fetchone()
        print(user)
        return jsonify ({
                "message": 'Login Succesful',
                "user_id": user["id"]
            }), 200
    
    except:
        return jsonify ({"message":"login failed"})
    
@app.route('/data-user/<int:user_id>', methods=['GET'])
def show_site(user_id):
    user_id = int(user_id) - 1
    conn = pymysql.connect(
        host='localhost',
        password='',
        user='root',
        charset='utf8mb4',
        database='CVsitedb',
    )

    cursor = conn.cursor()
    sql = "SELECT * FROM photo_CV where uid = %s"
    cursor.execute(sql, (user_id))
    user_foto = cursor.fetchall()

    sql2 = "SELECT * FROM isi_CV where uid = %s"
    cursor.execute(sql2, (user_id))
    user_isi = list(cursor.fetchall())
    comma = ','
    array_of_kategori_isi = []
    for item in user_isi:
        item = list(item)
        id_isi = item[0]
        kategori = item[2]
        isi = item[3]
        if comma in isi:
            isi_list = list(isi.split(','))
            array_of_kategori_isi.append([id_isi, kategori, isi_list])
        else:
            array_of_kategori_isi.append([id_isi, kategori, [isi]])
        print(array_of_kategori_isi)
    return jsonify ({
        "user_foto": user_foto,
        "user_isi": array_of_kategori_isi
    }), 200

@app.route('/add-item/<int:user_id>', methods=['POST'])
def add_item(user_id):
    user_id = int(user_id) - 1
    data = request.get_json()
    kategori = data.get('kategori')
    isi = data.get('isi')

    try:
        conn = pymysql.connect(
            host='localhost',
            password='',
            user='root',
            charset='utf8mb4',
            database='CVsitedb',
        )

        cursor = conn.cursor()
        sql = "INSERT INTO isi_CV (uid, kategori, isi) VALUES (%s, %s, %s)"
        cursor.execute(sql, (user_id, kategori, isi))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "item created"}), 201
    except Exception as e:
        return jsonify({"error bang":str(e)}), 500

@app.route('/update-item/<int:user_id>', methods=['PUT'])
def update_item(user_id):
    user_id = int(user_id) - 1
    data = request.get_json()
    kategori = data.get('kategori')
    isi = data.get('isi')
    kategori_lama = data.get('kategori_lama')
    isi_lama = data.get('isi_lama')

    try:
        conn = pymysql.connect(
            host='localhost',
            password='',
            user='root',
            charset='utf8mb4',
            database='CVsitedb',
        )
        
        cursor = conn.cursor()
        sql= "UPDATE isi_CV SET kategori=%s, isi=%s WHERE uid=%s AND kategori=%s AND isi=%s"
        cursor.execute(sql, (kategori, isi, user_id, kategori_lama, isi_lama))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Section Updated"}), 201
    except Exception as e:
        return jsonify({'error bang':str(e)}), 500
    

@app.route('/delete-item/<int:user_id>', methods=['DELETE'])
def delete_item (user_id):
    user_id = int(user_id) - 1
    data = request.get_json()
    isi = data.get('isi')
    kategori = data.get('kategori')

    try: 
        conn = pymysql.connect(
        host='localhost',
        password='',
        user='root',
        charset='utf8mb4',
        database='CVsitedb',
    )
        
        cursor = conn.cursor()
        sql = "DELETE FROM isi_CV WHERE isi=%s and kategori=%s"
        cursor.execute(sql, (isi, kategori))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return jsonify({'error bang:', str(e)}), 500

if __name__ == "__main__":
    initialize_db()
    insert_db()
    app.run(debug=True)


    
