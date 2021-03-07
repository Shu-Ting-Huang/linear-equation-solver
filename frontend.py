import os
def frac2latex(x):
    if x.q == 1:
        return str(x.p)
    elif x.p > 0:
        return '\\frac{' + str(x.p) + "}{" + str(x.q) + "}"
    else:
        return '-\\frac{' + str(-x.p) + "}{" + str(x.q) + "}"

def frac2latex_omit1(x):
    if x == 1:
        return ""
    elif x == -1:
        return "-"
    elif x.q == 1:
        return str(x.p)
    elif x.p>0:
        return '\\frac{' + str(x.p) + "}{" + str(x.q) + "}"
    else:
        return '-\\frac{' + str(-x.p) + "}{" + str(x.q) + "}"

def matrix2latex(A, bar_config=''): #bar_config indicate where to put vertical bar. Input format like "[ccc|c]"
    (m,n) = A.shape
    result = '\\begin{pmatrix}' + bar_config + '\n'
    for i in range(m): #i row through rows of A
        for j in range(n-1): #j row through columns of A except the last one
            result += (frac2latex(A[i,j]) + ' & ')

        #dealing with the last column
        if i != m-1: #not the last row
            result += (frac2latex(A[i,n-1]) + '\\\\[4pt]\n')
        else: #the last row
            result += (frac2latex(A[i,n-1]) + '\n')
    result += '\\end{pmatrix}\n'
    return result

def row_op_type2latex(row_op):
    if row_op['op'] == 'n->n+km':
        k = row_op['k']
        m = row_op['row2'] + 1
        n = row_op['row'] + 1
        return frac2latex_omit1(k) + 'R_{' + str(m) + '}+R_{' + str(n) + '}\\rightarrow R_{' + str(n) +'}'
    elif row_op['op'] == 'n<->m':
        m = row_op['row1'] + 1
        n = row_op['row2'] + 1
        return 'R_{' + str(m) + '}\\leftrightarrow R_{' + str(n) + '}'
    else:
        k = row_op['k']
        n = row_op['row'] + 1
        return frac2latex_omit1(k) + 'R_{' + str(n) + '}\\rightarrow R_{' + str(n) + '}'

def output2pdf(B,bar_config=''):
    with open('output.tex','w') as f:
        f.write("\\documentclass[english]{article}\n")
        f.write("\\usepackage{amsfonts}\n")
        f.write("\\usepackage{amsmath}\n")
        f.write("\\allowdisplaybreaks\n")
        f.write("\\makeatletter\n")
        f.write("\\renewcommand*\\env@matrix[1][*\\c@MaxMatrixCols c]{%\n")
        f.write("  \\hskip -\\arraycolsep\n")
        f.write("  \\let\\@ifnextchar\\new@ifnextchar\n")
        f.write("  \\array{#1}}\n")
        f.write("\\makeatother\n\n")
        f.write("\\begin{document}\n\n")
        f.write("\\title{Solution}\n")
        f.write("\\maketitle\n\n")
        f.write("\\begin{align*}\n")

        #Write the initial matrix:
        f.write('&'+matrix2latex(B.mat_seq[0], bar_config=bar_config))

        #Write down each row operation step:
        for t in range(len(B.row_op_seq)):
            f.write('\\'+'\\'+'\n\\xrightarrow{' + row_op_type2latex(B.row_op_seq[t]) + '}\n&' \
                    + matrix2latex(B.mat_seq[t+1], bar_config=bar_config))
        
        f.write('\\end{align*}\n\\end{document}')
    os.system('pdflatex output.tex')
    os.remove("output.aux")
    os.remove("output.log")
    # os.system("start SumatraPDF output.pdf")
    # os.system("pause")
