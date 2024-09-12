from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import List, Dict
from app.services.util import generate_unique_id, slot_not_available_error, event_not_found_error, \
    reminder_not_found_error, date_lower_than_today_error


@dataclass
class Reminder:
    EMAIL = "email"
    SYSTEM = "system"
    date_time: datetime
    type: str = EMAIL

    def __str__(self):
        return f"Reminder on {self.date_time} of type {self.type}"

@dataclass
class Event:
    title: str
    description: str
    date_: date
    start_at: time
    end_at: time
    reminders: List[Reminder] = field(default_factory=list)
    id: str = field(default_factory=generate_unique_id)

    def add_reminder(self, date_time: datetime, type_: str = Reminder.EMAIL):
        reminder = Reminder(date_time=date_time, type=type_)
        self.reminders.append(reminder)

    def delete_reminder(self, reminder_index: int):
        if 0 <= reminder_index < len(self.reminders):
            del self.reminders[reminder_index]
        else:
            reminder_not_found_error()

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Event title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Time: {self.start_at} - {self.end_at}")


