
def outerclosures():
    message = "this is from closures"
    def innerclosures():
        print(message)
    return innerclosures

outerfunc = outerclosures()

print(outerfunc.__name__)
