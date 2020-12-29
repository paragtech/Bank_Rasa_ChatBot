# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from product_predict import Product


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_group"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data=tracker.latest_message['text']

        details = data.split()
        gender = details[0]
        age = details[1]
        balance = details[2]
        group = Product(gender,age,balance)
        dispatcher.utter_message(group)

        return []
