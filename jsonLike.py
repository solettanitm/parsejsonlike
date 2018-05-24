#!/usr/local/bin/python3
import fileinput, json


for line in fileinput.input():
    try:
        jsonObj = json.loads(line, encoding='utf-8')
        print(json.dumps(jsonObj, sort_keys=False, indent=2))
    except json.decoder.JSONDecodeError:
        indent = '  '
        head_idx = 0;
        txt_comma_list = line.split(',')
        for tc in txt_comma_list:
            if '{' in tc and txt_comma_list.index(tc) == 0:
                head_idx += 1
                print('{}{}{}{}{}'.format(tc[:tc.index('{')+1].strip(), '\n', indent * head_idx, tc[tc.index('{')+1:].strip(), ','))
            elif '{' in tc and txt_comma_list.index(tc) != 0:
                print('{}{}{}{}{}{}'.format(indent * head_idx, tc[:tc.index('{')+1].strip(), '\n', indent * (head_idx + 1), tc[tc.index('{')+1:].strip(), ','))
                head_idx += 1
            elif '{' not in tc and '}' not in tc:
                print('{}{}{}'.format(indent * head_idx, tc.strip(), ','))
            elif '}' in tc and txt_comma_list.index(tc) != (len(txt_comma_list) - 1):
                if len(tc.split('}')) > 2:  # a:{a1:{b1, b2}},
                    for index, tail in enumerate(tc.split('}')):
                        print('{}{}{}{}{}'.format(indent * head_idx, tail[:index-1].strip(), '\n', indent * (head_idx - index - 1), '},'))
                        head_idx -= 1
                else:  # a:{a1:{b1, b2}, a2},
                    print('{}{}{}{}{}'.format(indent * head_idx, tc[:tc.index('}')].strip(), '\n', indent * (head_idx - 1), '},'))
                    head_idx -= 1
            elif '}' in tc and txt_comma_list.index(tc) == (len(txt_comma_list) - 1):
                print('{}{}{}{}'.format(indent * head_idx, tc[:len(tc)-1].strip(), '\n', tc[len(tc)-1]))





