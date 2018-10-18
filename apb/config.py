import configparser, os

rc = os.path.join(os.path.dirname(__file__), 'apbrc')
conf = configparser.ConfigParser()

def read(section, setting):
    conf.read(rc)
    value = conf[section][setting]
    if ', ' in value:
        value = value.split(', ')

    return value
