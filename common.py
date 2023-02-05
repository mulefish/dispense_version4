# Thanks Stackoverflow!
# https://stackoverflow.com/questions/9781218/how-to-change-node-jss-console-font-color
Reset = "\x1b[0m"
Bright = "\x1b[1m"
Dim = "\x1b[2m"
Underscore = "\x1b[4m"
Blink = "\x1b[5m"
Reverse = "\x1b[7m"
Hidden = "\x1b[8m"

FgBlack = "\x1b[30m"
FgRed = "\x1b[31m"
FgGreen = "\x1b[32m"
FgYellow = "\x1b[33m"
FgBlue = "\x1b[34m"
FgMagenta = "\x1b[35m"
FgCyan = "\x1b[36m"
FgWhite = "\x1b[37m"

BgBlack = "\x1b[40m"
BgRed = "\x1b[41m"
BgGreen = "\x1b[42m"
BgYellow = "\x1b[43m"
BgBlue = "\x1b[44m"
BgMagenta = "\x1b[45m"
BgCyan = "\x1b[46m"
BgWhite = "\x1b[47m"

def o2j(list_of_objs):
    j = json.dumps( list_of_objs )
    return j 



def magenta(msg): 
    x = "{}{}{}{}".format(BgMagenta, FgBlack, msg, Reset)
    print(x)

def yellow(msg):
    x = "{}{}{}{}".format(BgYellow, FgBlack, msg, Reset)
    print(x)


def green(msg):
    x = "{}{}{}{}".format(BgGreen, FgBlack, msg, Reset)
    print(x)


def cyan(msg):
    x = "{}{}{}{}".format(BgCyan, FgBlack, msg, Reset)
    print(x)


def log(msg):
    print(msg)

def verdict(a, b, msg):
    if a == b:
        cyan("PASS " + msg )
    else:
        yellow("FAIL " + msg)

def getUsers():
    users = {}
    users["a"] = "a"
    users["kermitt"] = "Happy$100"
    users["Shabone"] = "bonny"
    users["Eeboo"] = "boo"
    users["Maggy"] = "arrawarrru"
    users["Mr. C"] = "meow"
    return users

