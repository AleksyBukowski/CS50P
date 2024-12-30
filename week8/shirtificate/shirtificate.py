from fpdf import FPDF

def main():
    name = input("Name: ")
    create_shirt(name)


def create_shirt(name):
    # A4 is 210 x 297
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()

    pdf.set_font(family="Times", size=60)
    pdf.cell(text="CS50 Shirtificate", h=55, center=True)

    # Width is set to 190, which gives us two paddings of 10 at the left and right (x=10)
    pdf.image("shirtificate.png", x=10, y=70, w=190)

    pdf.set_font(family="Helvetica", style="b", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(text=f"{name.title()} took CS50", h=250, center=True)

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
