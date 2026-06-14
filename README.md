Library Project

מערכת ניהול ספרייה
כולל דאטה בייס המכיל מידע על כל הספרים שבספריה וכל החברים הרשומים

המערכת מאפשרת לנהל את מאגרי הספרים ולפקח על שאילת והחזרת הספרים למנויים

__כלים__
המערכת נכתבה בפייתון, וכוללת שימוש ב
FastAPI
Docker
mysql.connector


__מבנה תיקיות__
library-api/
│
│
├── main.py
├── database/
│ ├── db_connection.py
│ ├── book_db.py
│ └── member_db.py
├── routes/
│ ├── book_routes.py
│ ├── member_routes.py
│ └── report_routes.py
├── logs/
│ └── app.log
│
├── README.md
├── requirements.txt
└── .gitignore

__טבלאות__
books:
id, title, author, genre, is_available, id_member_by_borrowed 

members:
id, name, email, is_active, total_borrows

__הוראות הרצה__
git clone https://github.com/elchanan003/library_project.git

docker run --name my-sql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql

pip install -r requirements.txt
uvicorn main:app --reload



המערכת תהיה זמינה בכתובת
http://127.0.0.1:8000