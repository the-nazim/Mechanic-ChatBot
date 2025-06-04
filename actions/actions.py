# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionEVDiagnosis(Action):

    def name(self) -> Text:
        return "action_ev_diagnosis"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_message = tracker.latest_message.get('text', '').lower()

        if "charging" in user_message:
            dispatcher.utter_message(text="Check if the charging cable is securely connected and the station is functional.")
        elif "battery" in user_message:
            dispatcher.utter_message(text="Battery degradation might be the issue. Consider checking the battery health report.")
        elif "motor" in user_message:
            dispatcher.utter_message(text="You might be facing motor controller issues. Please consult a technician.")
        else:
            dispatcher.utter_message(text="I need more details to assist you with the EV issue.")

        return []            

