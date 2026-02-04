% Dirk Stratmann
% Janvier 2026
% dirk.stratmann at upmc.fr

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{TP}[une classe Latex pour les comptes rendu de TP]
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}

\LoadClass[17pt]{extarticle}
\usepackage{lmodern}
%\usepackage{booktabs}
%\usepackage{setspace}
\usepackage[french]{babel}
\usepackage{hyperref}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{multicol}
\usepackage{paracol}
\setlength{\columnsep}{2em}

\usepackage{enumitem}
\usepackage{pifont}
\usepackage{amssymb}  % for \checkmark

% Support for Unicode characters like checkmarks in minted code
\usepackage{newunicodechar}
\newunicodechar{✓}{\checkmark}

%\setlength{\abovecaptionskip}{2pt plus 3pt minus 2pt}
%\setlength{\belowcaptionskip}{2pt plus 3pt minus 2pt}

% 16:10 landscape page format (same height as A4 landscape):
\RequirePackage[paperheight=18.9cm, paperwidth=33.6cm, left=2cm,right=2cm,top=1.5cm,bottom=2cm]{geometry}


\usepackage{xcolor}

\usepackage{titlesec}

\titleformat{\section}{\normalfont \Large \bfseries}
{Question\ \thesection}{2.3ex plus .2ex}{}
\titlespacing{\subsection}{2em}{*1}{*1}


\newcommand{\entete}[4]{
    \begin{flushleft}
    Nom étudiant: #1\\
    Numéro étudiant: #2
    \end{flushleft}

    \begin{center}\vspace{-1.5cm}
    \textbf{\large #3} \\
    \textbf{#4}
    \end{center}

    \noindent\rule{\linewidth}{.6pt}
}



%%% minted stuff
\usepackage{minted}
\usepackage{mdframed} % for pythonfile listings with more than one page

%%%%%%%%%%%%%%%%%%%%%%%
%% Automatic line breaking as in the new minted version 2.0  
%% https://github.com/gpoore/minted
%% "breaklines" option
%%%%%%%%%%%%%%


%\usemintedstyle{trac}
%\usemintedstyle{bw}
%\usemintedstyle{colorful}
%\usemintedstyle{friendly}
%\usemintedstyle{borland}
%\usemintedstyle{manni}
%\usemintedstyle{rrt}
%\usemintedstyle{monokai}
%\usemintedstyle{perldoc}
%\usemintedstyle{default}
%\usemintedstyle{murphy}
\usemintedstyle{vs}  % Clean, professional Visual Studio style
%\usemintedstyle{tango}
%\usemintedstyle{fruity}
%\usemintedstyle{autumn}
%\usemintedstyle{emacs}
%\usemintedstyle{vim}
%\usemintedstyle{pastie}
%\usemintedstyle{native}

%\usepackage[gray]{xcolor}
%\setmonofont[Scale=0.9,BoldFont={Inconsolata Bold}]{Inconsolata}

\definecolor{mintedbackground}{rgb}{0.98,0.98,0.98}  % Almost white, clean background
\definecolor{codeborder}{rgb}{0.6,0.6,0.65}  % Subtle gray border
\definecolor{linenumcolor}{rgb}{0.5,0.5,0.5}  % Medium gray line numbers

\newminted{python}{
bgcolor=mintedbackground,
fontfamily=tt,
linenos=true,
numberblanklines=true,
numbersep=10pt,
gobble=0,
frame=lines,
framerule=0.6pt,
framesep=3mm,
rulecolor=codeborder,
funcnamehighlighting=true,
tabsize=4,
obeytabs=false,
mathescape=false,
samepage=false,
showspaces=false,
showtabs=false,
texcl=false,
breaklines=true,
breakanywhere=false,
breakbytoken=true
}

\newmintedfile{py}{
bgcolor=mintedbackground,
fontsize=\normalsize,
baselinestretch=1.05,
fontfamily=tt,
linenos=true,
numberblanklines=true,
numbersep=10pt,
gobble=0,
frame=single,
framerule=0.6pt,
framesep=3mm,
rulecolor=codeborder,
funcnamehighlighting=true,
tabsize=4,
obeytabs=false,
mathescape=false,
samepage=false,
showspaces=false,
showtabs=false,
texcl=false,
breaklines=true,
breakbefore=.,
breakafter=-/,
breakbytoken=true
}

\newmint{python}{
%bgcolor=mintedbackground,
fontfamily=tt,
funcnamehighlighting=true,
tabsize=4,
obeytabs=false,
mathescape=false,
showspaces=false,
showtabs =false,
frame=leftline,
framerule=0.4pt,
framesep=4mm,
breaklines=true % new option in minted 2.0
}

% for pythonfile listings with more than one page
\newcommand{\pythonfile}[1]{
\mdfsetup{
  frametitle={\colorbox{codeborder!20}{\space\texttt{#1}\space}},
  frametitlealignment=\raggedright
}
\begin{mdframed}[
  linecolor=codeborder,
  topline=true,
  bottomline=true,
  leftline=false,
  rightline=false,
  linewidth=0.6pt,
  backgroundcolor=mintedbackground,
  userdefinedwidth=\linewidth,
  roundcorner=2pt,
  innertopmargin=5pt,
  innerbottommargin=5pt
]
   \pyfile{#1}
\end{mdframed}
}

\newcommand{\pythonmulti}[1]{
\textbf{#1}
%\begin{multicols}{2}
   \pyfile{#1}
%   \end{multicols}
}

\makeatletter
\newenvironment{programme}[1]{
   \protected@edef\@currentlabelname{#1}
   \protected@edef\@currentlabel{#1}
   \phantomsection
   \label{#1}
 }
 \makeatother

\newcommand{\prog}[1]{
\begin{programme}{#1}
\pythonfile{#1}
\end{programme}
}

\newcommand{\progSnippet}[3]{
\textbf{#1}
\pyfile[firstline=#2,lastline=#3]{#1}
}

\newcommand{\progLong}[1]{
\begin{programme}{#1}
\pythonmulti{#1}
\end{programme}
}

\newcommand{\progLongSnippet}[3]{
\begin{programme}{#1}
\textbf{#1}
\begin{multicols}{2}
   \pyfile[firstline=#2,lastline=#3]{#1}
\end{multicols}
\end{programme}
}

\renewcommand{\theFancyVerbLine}{\sffamily\textcolor{linenumcolor}{\scriptsize\arabic{FancyVerbLine}}}

%%%%% minted stuff end
