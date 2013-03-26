import subprocess
import os
import shlex
from XCat_tex_Construction import Report_File

def Creat_Report(Halo,Input,Output):
    print "Creating report ..."
    Report_File(Halo,Input,Output)
    proc=subprocess.Popen(shlex.split('pdflatex Report/report.tex'))
    proc.communicate()
    proc=subprocess.Popen(shlex.split('pdflatex Report/report.tex'))
    proc.communicate()
    proc=subprocess.Popen(shlex.split('cp report.pdf Report'))
    proc.communicate()
    os.unlink('report.aux')
    os.unlink('report.log')
    os.unlink('report.out')
    os.unlink('report.pdf')
    
    print "Report is created successfully."
    
