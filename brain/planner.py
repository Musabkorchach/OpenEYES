"""
==================================================
OpenEyes Vision OS

Module : Planner Engine
Version: 0.2

Description:
Creates a simple action plan based on reasoning facts.
==================================================
"""


class PlannerEngine:

    def create_plan(self, facts):

        plan = []

        for fact in facts:

            if fact == "Person detected":
                plan.append("person_detected")

            if fact == "A person may be sitting":
                plan.append("observe_person_posture")

            if fact == "A person may be watching a screen":
                plan.append("observe_screen_activity")

            if fact == "Scene is empty":
                plan.append("continue_scanning")

        if not plan:
            plan.append("continue_observing")

        return plan