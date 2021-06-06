keywords = ['gifbot']

def help(keyword=''):
    """Filter for general help or specific keyword help."""
    if not keyword:
        file = open('help/help.md')
        contents = file.read()
        return (contents)
    if keyword[0]:
        keyword = str.lower(keyword)
        if keyword in keywords:
            document = 'help/help_' + keyword + '.md'
            print(document)
            file = open(document, 'r')
            contents = file.read()
            return (contents)
        else:
            file = open('help/help.md')
            contents = file.read()
            return (contents)