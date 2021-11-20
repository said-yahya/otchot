from django.db import connection


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()]


def dictfetchone(cursor):
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))


def get_otchot(id):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            select * from mainapp_otchot 
            where id='{id}' 
        """)
        data = dictfetchone(cursor)
    return data


def get_otchot_all():
    with connection.cursor() as cursor:
        cursor.execute(f"""
            select * from mainapp_otchot
            order by created_date DESC  
        """)
        data = dictfetchall(cursor)
    return data


def get_otdels(id):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            select * from mainapp_otdel
            where otchot_id='{id}'
            order by created_date ASC  
        """)
        data = dictfetchall(cursor)
    return data

