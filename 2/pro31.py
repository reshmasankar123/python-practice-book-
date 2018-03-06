def parse(filename, separator_key, comment_key):
    f = open(filename)
    if not f:
        print("No file")
        return 1

    out_list     = []
    current_list = []
    lines = []
    lines_to_parse = []
    current_line = ''

    symbol_index = 0
    line_index = 0

    for line in f:
        lines.append(line)

    while line_index < len(lines):
        while symbol_index < len(lines[line_index]):
            current_symbol = lines[line_index][symbol_index]
            if current_symbol == '#':
#                if line_index + 1 == len(lines):
#                    symbol_index = len(lines[line_index])
                symbol_index = 0
                line_index += 1 
            else:
                current_line += current_symbol
                symbol_index += 1
        lines_to_parse.append(current_line)
        current_line = ''
        line_index += 1
        symbol_index = 0

    for line in lines_to_parse:
        for symbol in line:
            if symbol != '\n' and symbol != separator_key:
                current_list.append(symbol)
        out_list.append(current_list)
        current_list = []
    return out_list

#print(parse('a.csv', '!', '#'))def parse(filename, separator_key, comment_key):
    f = open(filename)
    if not f:
        print("No file")
        return 1

    out_list     = []
    current_list = []
    lines = []
    lines_to_parse = []
    current_line = ''

    symbol_index = 0
    line_index = 0

    for line in f:
        lines.append(line)

    while line_index < len(lines):
        while symbol_index < len(lines[line_index]):
            current_symbol = lines[line_index][symbol_index]
            if current_symbol == '#':
#                if line_index + 1 == len(lines):
#                    symbol_index = len(lines[line_index])
                symbol_index = 0
                line_index += 1 
            else:
                current_line += current_symbol
                symbol_index += 1
        lines_to_parse.append(current_line)
        current_line = ''
        line_index += 1
        symbol_index = 0

    for line in lines_to_parse:
        for symbol in line:
            if symbol != '\n' and symbol != separator_key:
                current_list.append(symbol)
        out_list.append(current_list)
        current_list = []
    return out_list
print(parse('a.txt', '!', '#'))