mport json

def super_json_loads(text):
    json_objects = []
    start_chars = "{["
    end_chars = "}]" 

    # Replace all newlines in the text to make it single-line
    text = text.replace("\n", "\\n")

    i = 0
    while i < len(text):
        # Find the start of a JSON object or array
        start_index = text.find(start_chars[0], i) if "{" in text[i:] else len(text)
        array_start_index = text.find(start_chars[1], i) if "[" in text[i:] else len(text)

        # Select the nearest start character
        i = min(start_index, array_start_index)
        if i == len(text):
            break

        start_char = text[i]
        end_char = end_chars[start_chars.index(start_char)]

        count = 1
        j = i + 1

        # Find the matching end character
        while j < len(text) and count > 0:
            next_start = text.find(start_char, j)
            next_end = text.find(end_char, j)

            if next_start == -1:
                next_start = len(text)
            if next_end == -1:
                next_end = len(text)

            if next_start < next_end:
                count += 1
                j = next_start + 1
            else:
                count -= 1
                j = next_end + 1

        # Extract and decode the JSON object
        try:
            json_obj = json.loads(text[i:j])
            json_objects.append(json_obj)
        except json.JSONDecodeError:
            pass

        i = j - 1

    if len(json_objects) == 1:
        return json_objects[0]
    return json_objects

# Example usage
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
