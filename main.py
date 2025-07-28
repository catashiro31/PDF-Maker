from fpdf import FPDF
import pandas as pd

data = pd.read_csv('topics.csv',sep=',')
pdf = FPDF(orientation="P",unit='mm',format='a4')
pdf.set_auto_page_break(auto=False)

for index, row in data.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times',style='B',size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row['Topic'].upper(),border=0,ln=1,align='L')
    pdf.line(x1=10,y1=25,x2=200,y2=25)
    pdf.ln(265)
    pdf.set_font(family='Times',style='',size=12)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row['Topic'],border=0,ln=1,align='R')

    for i in range(row['Pages']-1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family='Times', style='', size=12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row['Topic'], border=0, ln=1, align='R')

pdf.output('output.pdf')