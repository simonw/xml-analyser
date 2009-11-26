xml_analyser.py
===============

A simple tool for counting the number of different child / parent / attributes
in use for an arbitrary XML file.

Usage:

python xml_analyser.py example.xml

If example.xml looks like this:

<example>
  <foo>
    <bar a="1" b="2">
      <baz />
    </bar>
  </foo>
  <foo>
    <bar a="1" b="2" c="3" />
  </foo>
</example>

xml_analyser outputs this:

{'bar': {'attr_counts': {'a': 2, 'b': 2, 'c': 1},
         'child_counts': {'baz': 1},
         'parent_counts': {'foo': 2}},
 'baz': {'attr_counts': {}, 'child_counts': {}, 'parent_counts': {'bar': 1}},
 'example': {'attr_counts': {},
             'child_counts': {'foo': 2},
             'parent_counts': {}},
 'foo': {'attr_counts': {},
         'child_counts': {'bar': 2},
         'parent_counts': {'example': 2}}}
