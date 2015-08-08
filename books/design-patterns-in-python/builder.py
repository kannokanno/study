class Director:
    def construct(builder):
        builder.open()
        builder.make_title('Good Title')
        builder.make_body('Nice Body')
        builder.close()
        return builder

    construct = staticmethod(construct)


class HTMLBuilder:
    def __init__(self):
        self.text = ''

    def open(self):
        self.text += "<html>\n"

    def close(self):
        self.text += "</html>\n"

    def make_title(self, str):
        self.text += "  <title>%s</title>\n" % str

    def make_body(self, str):
        self.text += "  <body>%s</body>\n" % str

    def get_result(self):
        return self.text


class XMLBuilder:
    def __init__(self):
        self.text = ''

    def open(self):
        self.text += "<xml>\n"

    def close(self):
        self.text += "</xml>\n"

    def make_title(self, str):
        self.text += "  <title name='title' value='%s'></title>\n" % str

    def make_body(self, str):
        self.text += "  <body name='body' value='%s'></body>\n" % str

    def get_result(self):
        return self.text

if __name__ == '__main__':
    print "==HTML=="
    print Director.construct(HTMLBuilder()).get_result()
    print "==XML=="
    print Director.construct(XMLBuilder()).get_result()
