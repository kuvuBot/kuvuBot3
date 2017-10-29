import datetime;

class Logger:
    def __init__(self, filename, format='%Y-%m-%d %H:%M:%S'):
        self.filename = filename
        self.format = format

    def log(self, message):
        print(datetime.datetime.now().strftime(self.format)+ ' ' + message)