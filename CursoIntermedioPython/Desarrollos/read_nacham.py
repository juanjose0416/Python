def readFile():
    text = []
    with open("./archivos/nacham_full_transactions_out.txt", "r", encoding="utf-8") as f:
        for line in f:
            text.append(line)
    return text;


def write(text):
    with open("./archivos/nacham_out_full_transactions_1.txt", "w", encoding="utf-8") as f:
            f.write(text)


def split_text(text):
    text = text[0]
    final_text = ""
    SIZE_BY_LINE = 106
    size_lines = int(len(text)/SIZE_BY_LINE)
    for i in range(size_lines):
        final_text = final_text + text[i*SIZE_BY_LINE:(SIZE_BY_LINE*(i+1))] + "\n"

    return final_text


if __name__ == '__main__':
    text_out = split_text(readFile());
    write(text_out)