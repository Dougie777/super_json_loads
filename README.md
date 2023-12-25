# super_json_loads
super_json_loads is an advanced JSON parsing function for Python, offering a drop in replacement for the standard python json.loads function. It is specifically adept at handling broken JavaScript that span across multiple lines, and handles multiple json occurances inside a string combining them into an array and ignoring non-json text.

Features
Multiple JSON Objects: Efficiently detects and parses multiple JSON objects or arrays embedded within a larger string, including broken JavaScript.
Multiline JSON Strings: Capable of handling JSON strings that span multiple lines, ensuring proper parsing and formatting.
Escaped Quotes Handling: Processes JSON strings with escaped quotes (\") accurately.
Newlines in JSON Strings: Converts actual line breaks in JSON strings to \n for correct JSON formatting and readability.
Installation
Copy the super_json_loads.py file into your project directory to use it.

Usage
super_json_loads can be used as a drop-in replacement for json.loads. It's particularly useful for parsing strings that represent broken JavaScript or contain multiple JSON structures:

python
Copy code
from super_json_loads import super_json_loads

# Example INVALID JSON string with multiple lines
json_string = """

Random text to be ignored...

{"text": "This is a string with a newline

character 
inside the quote"}

Some random text saying blah blah blah...

{"text": "This is a string with an escaped \\"qu
ote\\" inside"}

More random text ....

{"text": "This is a string with 'single quotes' and \\
"double quotes
\\" inside"}

Some other text
"""

# Use super_json_loads to parse
parsed_json = super_json_loads(json_string)
print(parsed_json)

Result
[{'text': 'This is a string with a newline\n\ncharacter \ninside the quote'}, 
{'text': 'This is a string with an escaped "qu\note" inside'}, 
{'text': 'This is a string with \'single quotes\' and "double quotes\n" inside'}]


Contributions
I welcome contributions, issues, and feature requests.

License
This project is distributed under the MIT License. See LICENSE for more information.
