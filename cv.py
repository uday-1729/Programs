from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors


def create_pdf():
    c = canvas.Canvas("test_cv.pdf", pagesize=letter)
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(300, 740, "Udayshankar Rajshekhar")

    c.setFillColor(colors.black)
    c.setFont("Helvetica", 12)
    c.drawCentredString(
        300, 700, "udayshankar.mlscma@learner.manipal.edu ; +91 - 9611509715"
    )

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 670, "Education")
    c.drawString(50, 150, "Technical Skills")

    c.setFont("Helvetica", 12)

    c.drawString(
        150,
        650,
        "Master of Science in Systems Biology, Manipal School of Life Sciences",
    )
    c.drawString(150, 630, "Manipal Academy of Higher Education, Manipal, India")

    c.setFont("Helvetica-Bold", 12)
    c.drawRightString(550, 610, "GPA : 8.29/10")
    c.drawString(60, 650, "2021 - 2023")

    c.setFont("Helvetica", 12)

    c.drawString(150, 590, "Bachelor of Technology in Biotechnology, PES University")
    c.drawString(150, 570, "Bangalore, India")

    c.setFont("Helvetica-Bold", 12)
    c.drawRightString(550, 550, "GPA : 7.20/10")
    c.drawString(60, 590, "2016 - 2020")
    c.drawString(60, 360, "Jan 2023 - Jun 2023")
    c.drawString(60, 500, "Oct 2021 - Oct 2020")
    c.drawString(60, 240, " Jan 2020 - March 2020")

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 520, "Work Experience")
    c.drawString(50, 400, "Projects and thesis")

    c.setFont("Helvetica", 12)

    c.drawString(200, 500, "Project Assistant")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(60, 480, "Guide")
    c.drawString(60, 460, "Institute")
    c.drawString(60, 440, "Project")
    c.drawString(60, 320, "Guide")
    c.drawString(60, 200, "Guide")

    c.drawString(60, 300, "Institute")
    c.drawString(60, 180, "Institute")

    c.setFont("Helvetica-Bold", 14)
    c.drawString(60, 380, "Masters dissertation")
    c.drawString(60, 260, "Bachelors Final Project")

    c.setFont("Helvetica", 12)
    c.drawString(200, 480, "Professor. Siddhartha P Sarma")
    c.drawString(200, 460, "Molecular Biohysics Unit, Indian Institute of Science")
    c.drawString(200, 300, "Molecular Biohysics Unit, Indian Institute of Science")
    c.drawString(200, 180, "Molecular Biohysics Unit, Indian Institute of Science")
    c.drawString(200, 440, "Recombinant expression and purification of conopeptides")
    c.drawString(200, 360, "Thesis titled 'Expression, purification and biophysical")
    c.drawString(200, 340, "studies of Conotoxins' ")
    c.drawString(200, 320, "Professor. Siddhartha P Sarma")
    c.drawString(200, 200, "Professor. Siddhartha P Sarma")

    c.drawString(200, 240, "Thesis titled 'Isolation and characterization")
    c.drawString(200, 220, "of bioactive peptides'")

    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, 120, "Biochemical and Biophysical Skills")

    c.setFont("Helvetica", 12)
    c.drawString(
        50,
        100,
        "SDS-PAGE , HPLC , FPLC , Circular Dichroism , UV- spectroscopy , Mass spectrometry,",
    )
    c.drawString(50, 80, "NMR spectroscopy (1D) , Thin Layer Chromatography. ")

    c.showPage()

    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, 720, "Molecular Biology Skills")
    c.drawString(50, 670, "Computational Skills")
    c.drawString(50 , 540 , "Languages")

    # c.setFont("Helvetica-Bold", 16)
    # c.drawString(50, 540, "General Skills")

    c.setFont("Helvetica", 12)
    c.drawString(
        50, 700, "Bacterial cell cultures , plasmid isolations , transformation, PCR."
    )
    c.drawString(
        50,
        650,
        "Proficient in Python and PERL , moderate understanding of R programming, ",
    )
    c.drawString(
        50,
        630,
        "using Linux based systems.Bioinformatics tools such as BLAST, Molecular",
    )
    c.drawString(
        50,
        610,
        "visualization tools such as PyMol, UCSF Chimera,Molecular dynamics using ",
    )
    c.drawString(
        50,
        590,
        "GROMACS , NGS data analysis. Competent at using software such as Microsoft office ,",
    )
    c.drawString(
        50, 570, "LaTex for document writing and plotting software such as LabPlot."
    )

    c.drawString(50, 520, "English , Kannada , Hindi")
    c.save()


if __name__ == "__main__":
    create_pdf()
 