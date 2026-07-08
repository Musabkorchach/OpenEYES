"""
==================================================
OpenEyes Vision OS

Module : World Model
Version: 0.3

Description:
Builds an internal representation of visible objects
and spatial relations between them.

Relations:
- near
- left_of
- right_of
- above
- below
- overlapping
==================================================
"""


class WorldModel:

    def __init__(self):
        self.objects = {}

    def update(self, tracked_objects):
        self.objects = {}

        for obj in tracked_objects:
            object_id = obj.get("id")
            name = obj.get("name", "object")
            center = obj.get("center")
            bbox = obj.get("bbox")

            if object_id is None or center is None or bbox is None:
                continue

            self.objects[object_id] = {
                "id": object_id,
                "name": name,
                "center": center,
                "bbox": bbox,
            }

        return self.snapshot()

    def snapshot(self):
        return {
            "objects": self.objects,
            "count": len(self.objects),
            "relations": self._build_relations(),
        }

    def _build_relations(self):
        relations = []
        objects = list(self.objects.values())

        for i in range(len(objects)):
            for j in range(i + 1, len(objects)):
                a = objects[i]
                b = objects[j]

                relation = self._relation_between(a, b)

                relations.append({
                    "object_a": f"{a['name']} #{a['id']}",
                    "object_b": f"{b['name']} #{b['id']}",
                    "relation": relation,
                })

        return relations

    def _relation_between(self, a, b):
        if self._overlap(a["bbox"], b["bbox"]):
            return "overlapping"

        ax, ay = a["center"]
        bx, by = b["center"]

        dx = bx - ax
        dy = by - ay

        abs_dx = abs(dx)
        abs_dy = abs(dy)

        if abs_dx < 100 and abs_dy < 100:
            return "near"

        if abs_dx > abs_dy:
            if dx > 0:
                return "left_of"
            return "right_of"

        if dy > 0:
            return "above"

        return "below"

    def _overlap(self, box_a, box_b):
        ax1, ay1, ax2, ay2 = box_a
        bx1, by1, bx2, by2 = box_b

        overlap_x = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_y = max(0, min(ay2, by2) - max(ay1, by1))

        overlap_area = overlap_x * overlap_y

        if overlap_area == 0:
            return False

        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)

        smaller_area = min(area_a, area_b)

        if smaller_area <= 0:
            return False

        overlap_ratio = overlap_area / smaller_area

        return overlap_ratio > 0.25