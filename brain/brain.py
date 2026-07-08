"""
==================================================
OpenEyes Vision OS

Module : Brain Engine

Version : 0.2

Description:
The Brain Engine is the central cognitive coordinator
of OpenEyes Vision OS.

Pipeline

Scene
    ↓
Knowledge
    ↓
Reasoning
    ↓
Planning
    ↓
Decision

==================================================
"""

from brain.knowledge import KnowledgeEngine
from brain.reasoning import ReasoningEngine
from brain.planner import PlannerEngine
from brain.decision import DecisionEngine


class OpenEyesBrain:

    def __init__(self):

        self.knowledge = KnowledgeEngine()
        self.reasoning = ReasoningEngine()
        self.planner = PlannerEngine()
        self.decision = DecisionEngine()

    def think(self, scene):

        # -----------------------------------------
        # Build Knowledge
        # -----------------------------------------

        knowledge = {}

        for object_name in scene.get("objects", {}):

            knowledge[object_name] = self.knowledge.describe(
                object_name
            )

        # -----------------------------------------
        # Logical Reasoning
        # -----------------------------------------

        facts = self.reasoning.analyze(scene)

        # -----------------------------------------
        # Planning
        # -----------------------------------------

        plan = self.planner.create_plan(facts)

        # -----------------------------------------
        # Decision
        # -----------------------------------------

        decision = self.decision.choose(plan)

        return {

            "scene": scene,

            "knowledge": knowledge,

            "facts": facts,

            "plan": plan,

            "decision": decision,

        }