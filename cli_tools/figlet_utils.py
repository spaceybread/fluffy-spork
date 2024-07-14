import pyfiglet

def figletCLI(message):
    f = pyfiglet.figlet_format(message)
    return "```" +  f + "```"