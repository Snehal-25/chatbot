import json
from typing import Any, Text, Dict, List
# from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionFindHotel(Action):

    def name(self) -> Text:
        return "action_find_hotels"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        _intent=tracker.latest_message['intent'].get('name')
        print("Intent of user message predicted by Rasa ",_intent)

        print(tracker.latest_message['text']) # to get user typed message
        intent_found = json.dumps(tracker.latest_message['response_selector'][_intent]['ranking'][0]['intent_response_key'], indent=4)
        print("retrieval we found (i.e intent response key ) ",intent_found)

        intent_found = f'utter_{eval(intent_found)}'
        dispatcher.utter_message(response = intent_found)

        dispatcher.utter_message(text="We are making a list of hotels for you...")

        return []