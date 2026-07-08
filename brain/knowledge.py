"""
==================================================
OpenEyes Vision OS

Module : Knowledge Engine

Version : 0.2

Description:
Provides a basic knowledge base about objects
detected in the scene.

Future versions will support:
- Knowledge Graph
- Semantic Relations
- Learning Database
- Pi Community Knowledge
==================================================
"""


class KnowledgeEngine:

    def __init__(self):

        self.knowledge = {

            "person": {
                "category": "living",
                "description": "A human being.",
                "can_move": True,
            },

            "chair": {
                "category": "furniture",
                "description": "Used for sitting.",
                "can_move": False,
            },

            "tv": {
                "category": "electronics",
                "description": "Displays visual media.",
                "can_move": False,
            },

            "laptop": {
                "category": "electronics",
                "description": "Portable computer.",
                "can_move": True,
            },

            "book": {
                "category": "education",
                "description": "Contains written knowledge.",
                "can_move": True,
            },
        }

    def describe(self, object_name):

        return self.knowledge.get(
            object_name,
            {
                "category": "unknown",
                "description": "Unknown object.",
                "can_move": False,
            },
        )

    def exists(self, object_name):

        return object_name in self.knowledge