import cowsay
import pyfiglet

def cowsayCLI(message):
    outer = "```"
    c = cowsay.get_output_string('cow', message)
    return outer + c + outer

def figletCLI(message):
    f = pyfiglet.figlet_format(message)
    return "```" +  f + "```"

print(cowsayCLI("hello"))
print(figletCLI("hello"))

