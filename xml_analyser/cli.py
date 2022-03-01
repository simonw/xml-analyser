import argparse
import json
import sys
from . import ElementStats, ET, truncate_xml
from xml.dom import minidom


def main(args=None, output=print):
    parser = argparse.ArgumentParser(
        description="Display a summary of elements in an XML file"
    )
    parser.add_argument("filepath", type=str, help="Path to the XML file")
    parser.add_argument(
        "--truncate",
        help="Output XML truncated to max of 2 repeats of each element",
        action="store_true",
    )
    res = parser.parse_args(args)
    if res.filepath == "-":
        fp = sys.stdin
    else:
        fp = open(res.filepath)
    try:
        et = ET.parse(fp)
    except Exception as e:
        print(e)
        sys.exit(1)
    if res.truncate:
        root = et.getroot()
        truncate_xml(root)
        _pretty_print(root)
        output(ET.tostring(root).decode("utf-8"))
    else:
        output(json.dumps(ElementStats(et).stats, indent=4))


def _pretty_print(current, parent=None, index=-1, depth=0):
    # https://stackoverflow.com/a/65808327/6083 - thanks, Tatarize
    for i, node in enumerate(current):
        _pretty_print(node, current, i, depth + 1)
    if parent is not None:
        if index == 0:
            parent.text = "\n" + ("  " * depth)
        else:
            parent[index - 1].tail = "\n" + ("  " * depth)
        if index == len(parent) - 1:
            current.tail = "\n" + ("  " * (depth - 1))
