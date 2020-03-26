import subprocess

def init_tr(tr_num_str):
    file_name = tr_num_str + "_task_report.tex"
    tr_file = open(file_name, 'w')
    tr_file.write("\\documentclass{article}\\usepackage[left=2cm,right=2cm,top=3cm]{geometry}\\usepackage[utf8]{inputenc}")
    tr_file.write("\\setlength{\\parindent}{0pt}")
    tr_file.write("\\usepackage{tabularx}")
    tr_file.write("\\begin{document}")
    return file_name

def finish_the_chili(tr):
    tr_file = open(tr, 'a')
    tr_file.write("\\end{document}")
    tr_file.close()
    try:
        subprocess.check_call(['pdflatex', tr])
    except:
        print("the chili went bad...")
