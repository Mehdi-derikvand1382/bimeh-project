import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# تنظیمات اتصال به پستگرس (با اطلاعات خودت)
DB_NAME = 'bimeh_db'
DB_USER = 'postgres'
DB_PASS = '1234' # رمز خودت را اینجا بگذار
DB_HOST = '127.0.0.1'
DB_PORT = '5432'

try:
    # اتصال به دیتابیس پیش‌فرض پستگرس
    conn = psycopg2.connect(dbname='postgres', user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    # قطع کردن اتصالات فعلی و پاک کردن دیتابیس
    print(f"در حال پاک کردن دیتابیس {DB_NAME}...")
    cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME} WITH (FORCE);")
    
    # ساخت مجدد دیتابیس
    print(f"در حال ساخت دیتابیس {DB_NAME}...")
    cursor.execute(f"CREATE DATABASE {DB_NAME};")
    
    print("✅ دیتابیس با موفقیت ریست شد!")
    cursor.close()
    conn.close()

except Exception as e:
    print(f"❌ خطا: {e}")