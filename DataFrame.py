class DataFrame:
    data = dict()
    
    def __init__(self, headers, data_lines, defaults, delimiter):
        self.headers = headers
        self.defaults = defaults
        self.delimiter = delimiter
        for line in data_lines:
            fields = line.split(delimiter)
            entry = {}
            for i,value in enumerate(fields):
                self.data.setdefault(headers[i].strip(),[]).append(value.strip())
