from sh import sed


def logi(msg):
    print( "[info] => " + msg )

def log(msg):
    print( "[log] => " + msg )

def loge(msg):
    print( "[error] => " + msg )

def replace(old, new, file):
    sed("-i", "s/{}/{}/g".format(old, new), file)
