# 11. Měj seznam slov a vypiš pouze ta, která mají víc než 4 znaky.

def seznam_slov():
    seznam_slov = ["holaho", "brambora", "syn", "vrt", "vlasy", "prd", "list"]
    novy_seznam_slov = []
    for i in seznam_slov:
        if len(i) > 4:
            novy_seznam_slov.append(i)

    print(f"původní seznam slov: {seznam_slov}")
    print(f"slova co mají víc než 4 znaky: {novy_seznam_slov}")


if __name__ == '__main__':
    seznam_slov()
