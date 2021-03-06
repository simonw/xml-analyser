from xml_analyser.cli import main
import pathlib
import sys

example_xml = pathlib.Path(__file__).parent / "example.xml"


def capture(stats):
    assert tuple(stats.items()) == tuple(
        {
            "example": {
                "count": 1,
                "parent_counts": {},
                "attr_counts": {},
                "child_counts": {"atop": 1, "foo": 2},
            },
            "atop": {
                "count": 1,
                "parent_counts": {"example": 1},
                "attr_counts": {"title": 1},
                "child_counts": {},
            },
            "bar": {
                "count": 2,
                "parent_counts": {"foo": 2},
                "attr_counts": {"a": 2, "b": 2, "c": 1},
                "child_counts": {"baz": 2},
            },
            "foo": {
                "count": 2,
                "parent_counts": {"example": 2},
                "attr_counts": {},
                "child_counts": {"bar": 2, "baz": 1},
            },
            "baz": {
                "count": 3,
                "parent_counts": {"bar": 2, "foo": 1},
                "attr_counts": {"d": 1},
                "child_counts": {},
                "count_with_text": 2,
                "max_text_length": 14,
            },
        }.items()
    )


def test_xml_analyser():
    main([str(example_xml)], capture)


def test_xml_analyser_stdin():
    old_stdin = sys.stdin
    sys.stdin = open(example_xml)
    main("-", capture)
