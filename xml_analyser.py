from xml.etree import ElementTree as ET

class ElementStats(object):
    def __init__(self, et):
        self.et = et
        self.stats = {}
        self.analyze()
    
    def analyze(self):
        "Count number of occurrences of each element"
        parent_lookups = {}
        for el in self.et.getiterator():
            parent = parent_lookups.get(el, None)
            tag = el.tag
            el_stats = self.stats.setdefault(tag, {})
            # Update parent count
            parent_counts = el_stats.setdefault('parent_counts', {})
            if parent:
                parent_counts[parent.tag] = parent_counts.get(parent.tag, 0)+1
            # Update attribute counts
            attr_counts = el_stats.setdefault('attr_counts', {})
            for attr in el.attrib:
                attr_counts[attr] = attr_counts.get(attr, 0) + 1
            # Update child counts
            child_counts = el_stats.setdefault('child_counts', {})
            for child in el.getchildren():
                child_counts[child.tag] = child_counts.get(child.tag, 0) + 1
                # Update parent_lookups while we're at it
                parent_lookups[child] = el

if __name__ == '__main__':
    import sys
    filename = sys.argv[-1]
    try:
        et = ET.parse(open(filename))
    except:
        print "Usage: %s <filename.xml>" % sys.argv[0]
        sys.exit(1)
    from pprint import pprint
    pprint(ElementStats(et).stats)
