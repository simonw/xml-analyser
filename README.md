# xml_analyser.py

A simple tool for showing various statistics about element usage in an 
arbitrary XML file.

Usage:

    xml-analyser example.xml

If example.xml looks like this:

```xml
<example>
  <foo>
    <bar a="1" b="2">
      <baz>This has text</baz>
    </bar>
  </foo>
  <foo>
    <bar a="1" b="2" c="3">
      <baz>More text here</baz>
    </bar>
    <baz d="1" />
  </foo>
</example>

xml_analyser outputs this:

    {'bar': {'attr_counts': {'a': 2, 'b': 2, 'c': 1},
            'child_counts': {'baz': 2},
            'count': 2,
            'parent_counts': {'foo': 2}},
    'baz': {'attr_counts': {'d': 1},
            'child_counts': {},
            'count': 3,
            'count_with_text': 2,
            'max_text_length': 14,
            'parent_counts': {'bar': 2, 'foo': 1}},
    'example': {'attr_counts': {},
                'child_counts': {'foo': 2},
                'count': 1,
                'parent_counts': {}},
    'foo': {'attr_counts': {},
            'child_counts': {'bar': 2, 'baz': 1},
            'count': 2,
            'parent_counts': {'example': 2}}}
