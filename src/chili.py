import subprocess

def init_tr(tr_num_str, short_date):
    file_name = tr_num_str + "_task_report.tex"
    tr_file = open(file_name, 'w')
    tr_file.write("\\documentclass{article}\\usepackage[left=2cm,right=2cm,top=3cm]{geometry}\\usepackage[utf8]{inputenc}")
    tr_file.write("\\setlength{\\parindent}{0pt}")
    tr_file.write("\\usepackage{tabularx}")
    tr_file.write("\\begin{document}")
    tr_file.write("\\begin{center}{\\Large\\hfill\\hfill Weekly Team Task Report  \\hfill " + tr_num_str + ", Wk " + tr_num_str + "}\\end{center}")

    tr_file.write("\\begin{center} \\def\\arraystretch{1.85} \\begin{tabular}{|p{5em}|p{5em}|p{5em}|p{5em}|p{5em}|} \\hline \\multicolumn{4}{|c|}{\\textbf{Team: }Astraea} & \\multicolumn{1}{|c|}{\\textbf{Date: } " + short_date + "}\\\\ \\hline\\multicolumn{5}{|c|}{\\textbf{Project Title: }Telescope Mirror Communication and Control System}\\\\\\hline \\textbf{Michael} & \\textbf{Peter} & \\textbf{Adam} & \\textbf{Trey} & \\textbf{Brandon} \\\\ Present & Present & Present & Present & Present \\\\ On-time & On-time & On-time & On-time & On-time \\\\\\hline \\end{tabular}\\end{center}")
    tr_file.close()
    return file_name

def recent_meetings(tr, list_of_meetings):
	tr_file = open(tr, 'a')
	tr_file.write("\\textbf{Recent Meetings:}\\\\")
	pot = list_of_meetings
	for chili in pot:
		tr_file.write(chili + "\\\\")
	tr_file.write("\\\\")
	tr_file.close()

def new_section(tr, section_name):
	tr_file = open(tr, 'a')
	tr_file.write("{\\Large\\textbf{" + section_name + ":}}\\\\")
	tr_file.close()

def new_task(tr, title, init, due, status, who, description, outcome):
	tr_file = open(tr, 'a')
	tr_file.write("\\begin{center}\\def\\arraystretch{1.85}\\begin{tabularx}{\\textwidth}{|X|X|X|X|}\\hline\\textbf{Task Title: }" + title + " & \\textbf{Task Initiation: }" + init + " & \\textbf{Orig. Due Date: }" + due + " & \\textbf{Status: }" + status + "\\% \\\\\\hline")
	tr_file.write("\\multicolumn{4}{|>{\\hsize=\\dimexpr4\\hsize+4\\tabcolsep+2\\arrayrulewidth\\relax}X|}{\\textbf{Who (\\%): }" + who + "}\\\\\\hline")
	tr_file.write("\\multicolumn{4}{|>{\\hsize=\\dimexpr4\\hsize+4\\tabcolsep+2\\arrayrulewidth\\relax}X|}{\\textbf{Description: }" + description + "}\\\\\\hline")
	tr_file.write("\\multicolumn{4}{|>{\\hsize=\\dimexpr4\\hsize+4\\tabcolsep+2\\arrayrulewidth\\relax}X|}{\\textbf{Outcome: }" + outcome + "}\\\\\\hline\\end{tabularx}\\end{center}")
	tr_file.close()

def finish_the_chili(tr):
    tr_file = open(tr, 'a')
    tr_file.write("\\end{document}")
    tr_file.close()
    try:
        subprocess.check_call(['pdflatex.exe', tr]) # pdflatex on linux, pdflatex.exe on wins, no idea for osx
    except:
        print("the chili went bad...")
