import cowsay

def cowsayCLI(message):
    outer = "```"
    c = cowsay.get_output_string('cow', message)
    return outer + c + outer

