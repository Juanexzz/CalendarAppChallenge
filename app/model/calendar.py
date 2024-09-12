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