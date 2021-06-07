from xml.etree import ElementTree as ET


class ElementStats(object):
    def __init__(self, et):
        self.et = et
        self.stats = {}
        self.analyze()

    def analyze(self):
        "Count number of occurrences of each element"
        parent_lookups = {}
        for el in self.et.iter():
            parent = parent_lookups.get(el, None)
            tag = el.tag
            el_stats = self.stats.setdefault(tag, {})
            el_stats["count"] = el_stats.get("count", 0) + 1
            # Update parent count
            parent_counts = el_stats.setdefault("parent_counts", {})
            if parent:
                parent_counts[parent.tag] = parent_counts.get(parent.tag, 0) + 1
            # Update attribute counts
            attr_counts = el_stats.setdefault("attr_counts", {})
            for attr in el.attrib:
                attr_counts[attr] = attr_counts.get(attr, 0) + 1
            # Update child counts
            child_counts = el_stats.setdefault("child_counts", {})
            for child in el:
                child_counts[child.tag] = child_counts.get(child.tag, 0) + 1
                # Update parent_lookups while we're at it
                parent_lookups[child] = el
            # If this has text, update text statistics
            if el.text is not None and not el.text.isspace():
                el_stats["count_with_text"] = el_stats.get("count_with_text", 0) + 1
                el_stats["max_text_length"] = max(
                    len(el.text), el_stats.get("max_text_length", 0)
                )
        # Sort results by their count, with parent counts as tie-breaker
        self.stats = dict(
            sorted(
                self.stats.items(),
                key=lambda p: (
                    p[1]["count"],
                    sum(p[1]["parent_counts"].values()),
                    p[0],
                ),
            )
        )
