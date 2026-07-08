"""
==================================================
OpenEyes Vision OS

Module : Decision Engine
Version: 0.2

Description:
Chooses safe and simple decisions based on facts,
knowledge, and scene understanding.
==================================================
"""


class DecisionEngine:

    def choose(self, plan):

        if not plan:
            return "observe"

        if "person_detected" in plan:
            return "focus_on_person"

        if "unknown_object" in plan:
            return "observe_unknown_object"

        return "continue_observing"