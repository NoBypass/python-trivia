def format_string(string):
    string = string.replace('&quot;', '"')
    string = string.replace('&amp;', '&')
    string = string.replace('&#039;', '\'')
    string = string.replace('&deg;', '°')
    string = string.replace('&shy;', '-')
    return string
