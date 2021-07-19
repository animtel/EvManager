from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet

from services.gcalendar import GCalendarMock


class ActionCheckWeather(Action):

    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text='Some weather')
        return []


class ActionGTimeSlots(Action):

    def name(self) -> Text:
        return "action_get_g_time_slots"

    def run(self, dispatcher, tracker, domain):
        # TODO: add google api module to get calendar events
        # TODO: add configurable get slots: daily, weekly, monthly
        # TODO: add global exception handler

        events_map = map(lambda x: x.__dict__, GCalendarMock().get_events())
        events = list(events_map)

        dispatcher.utter_message(text=str(events))
        return []


class ActionSendEmailTo(Action):

    def name(self) -> Text:
        return "action_send_email_to"

    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot('name')
        dispatcher.utter_message(text=f'Done! {email}')
        return [SlotSet('name', email)]
