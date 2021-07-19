from typing import List
from random import randrange
import datetime


class GCEvent:
    def __init__(self, name, description, date):
        self.name = name
        self.description = description
        self.date = date


class IGCalendar:
    def get_events(self, for_time_period_to=60 * 24) -> List[GCEvent]:
        """Load existed events from the calendar"""
        pass

    def create_event(self, event: GCEvent) -> GCEvent:
        """Create an event in calendar"""
        pass


class GCalendarMock(IGCalendar):
    def __init__(self):
        pass

    # mock some dates for 24 hours
    def _random_date(self, start, l, for_time):
        current = start
        dates = [current + datetime.timedelta(minutes=randrange(for_time)) for i in range(l)]

        return dates

    def get_events(self, for_time_period_to=60 * 24) -> List[GCEvent]:
        """Load existed events from the calendar"""
        startDate = datetime.datetime.now()
        how_many_events = 5

        return [GCEvent(f'Event #{i}', 'description', x.strftime("%d/%m/%y %H:%M")) for i, x in
                enumerate(self._random_date(startDate, how_many_events, for_time_period_to))]
