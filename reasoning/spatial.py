"""
==================================================
OpenEyes Vision OS

Module : Spatial Reasoning Engine
Version: 0.2

Description:
Analyzes spatial relationships between objects
inside the World Model.
==================================================
"""


class SpatialReasoningEngine:

    def analyze(self, world):
        relations = world.get("relations", [])

        insights = []

        for relation in relations:
            object_a = relation["object_a"]
            object_b = relation["object_b"]
            relation_type = relation["relation"]

            insights.append(
                f"{object_a} is {relation_type} {object_b}"
            )

        if not insights:
            insights.append("No spatial relationships detected.")

        return insights