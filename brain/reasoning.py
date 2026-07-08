"""
==================================================
OpenEyes Vision OS

Module : Reasoning Engine

Version : 0.2

Description:
Transforms scene information into logical facts.
==================================================
"""


class ReasoningEngine:

    def analyze(self, scene):

        facts = []

        people = scene.get("people", 0)
        chairs = scene.get("chairs", 0)
        screens = scene.get("screens", 0)

        if people > 0:
            facts.append("Person detected")

        if people > 0 and chairs > 0:
            facts.append("A person may be sitting")

        if people > 0 and screens > 0:
            facts.append("A person may be watching a screen")

        if scene["total_objects"] == 0:
            facts.append("Scene is empty")

        return facts