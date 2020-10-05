import colorama
import pydf
colorama.init()

print(colorama.Fore.BLUE+"Tiago Santos Batista")
print(colorama.Fore.BLACK+"Tiago Santos Batista")
print(colorama.Fore.CYAN+"Tiago Santos Batista")
print(colorama.Fore.RED+"Tiago Santos Batista")
print(colorama.Style.BRIGHT+"Tiago Santos Batista")
print(colorama.Back.BLUE+"Tiago Santos Batista")

pdf = pydf.generate_pdf('<h1>TiagoSantosBatista</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

