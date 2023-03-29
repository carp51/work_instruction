words = ["open", "closed", "casher", "stock_up", "eighteen", "other"]

for word in words:
    input_txt = word + "_input.txt" 
    with open(input_txt, encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
        f.close()

    # ファイルの中身を出力してみる
    print(lines)

    for i in range(len(lines)):
        if lines[i] == '':
            lines[i] = '<p>↓</p>'
            lines[i] += '\n'
        else:
            tmp = lines[i]
            tmp = list(tmp)
            
            tmp.insert(0, '<p>')
            tmp.append('</p>')
            tmp.append('\n')
            
            lines[i] = "".join(tmp)
            
    print(lines)
    
    output_txt = word + "_output.txt" 

    with open(output_txt, 'w', encoding='utf-8') as f:
        for content in lines:
            f.write(content)