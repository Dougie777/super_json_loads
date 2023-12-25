import json

def replace_newlines_in_json_strings(text):
    new_text = ""
    in_string = False
    escape_next = False
    for char in text:
        if char == '"' and not escape_next:
            in_string = not in_string
        elif char == '\\' and in_string:
            escape_next = True
            new_text += char
            continue
        elif char == '\n' and in_string:
            new_text += '\\n'
            escape_next = False
            continue

        escape_next = False
        new_text += char

    return new_text

def super_json_loads(text):
    json_objects = []
    start_chars = "{["
    end_chars = "}]"

    text = text.replace("\n\"", "\"")
    text = replace_newlines_in_json_strings(text)

    i = 0
    while i < len(text):
        start_index = text.find(start_chars[0], i) if "{" in text[i:] else len(text)
        array_start_index = text.find(start_chars[1], i) if "[" in text[i:] else len(text)

        i = min(start_index, array_start_index)
        if i == len(text):
            break

        start_char = text[i]
        end_char = end_chars[start_chars.index(start_char)]

        count = 1
        j = i + 1

        while j < len(text) and count > 0:
            next_start = text.find(start_char, j)
            next_end = text.find(end_char, j)

            next_start = next_start if next_start != -1 else len(text)
            next_end = next_end if next_end != -1 else len(text)

            if next_start < next_end:
                count += 1
                j = next_start + 1
            else:
                count -= 1
                j = next_end + 1

        try:
            json_obj = json.loads(text[i:j])
            json_objects.append(json_obj)
        except json.JSONDecodeError as e:
            print("JSON Decode Error:", e)
            print("Problematic text:", text[i:j])

        i = j - 1

    return json_objects[0] if len(json_objects) == 1 else json_objects

# Example usage
text_with_json = """

{
  "score": 2.0,
  "feedback": "hello
world
"
}

"""
result = super_json_loads(text_with_json)
print(result)

text_with_json = """

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
result = super_json_loads(text_with_json)
print(result)

