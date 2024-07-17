#!/usr/bin/env python3

import sqlite3

def init_db():
    conn = sqlite3.connect(r"jeevesbot/databases/reminders.db")
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        message TEXT,
        reminder_time TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

def add_reminder(user_id, message, reminder_time):
    conn = sqlite3.connect(r"jeevesbot/databases/reminders.db")
    c = conn.cursor()
    c.execute('INSERT INTO reminders (user_id, message, reminder_time) VALUES (?, ?, ?)', (user_id, message, reminder_time))
    conn.commit()
    conn.close()

def get_due_reminders(current_time):
    conn = sqlite3.connect(r"jeevesbot/databases/reminders.db")
    c = conn.cursor()
    c.execute('SELECT id, user_id, message FROM reminders WHERE reminder_time <= ?', (current_time,))
    reminders = c.fetchall()
    c.execute('DELETE FROM reminders WHERE reminder_time <= ?', (current_time,))
    conn.commit()
    conn.close()
    return reminders