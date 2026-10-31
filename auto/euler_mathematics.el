;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "euler_mathematics"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt" "letterpaper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("lmodern" "") ("geometry" "margin=1in" "headheight=14pt") ("amsmath" "") ("amssymb" "") ("amsthm" "") ("mathtools" "") ("fancyhdr" "") ("hyperref" "")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "inputenc"
    "fontenc"
    "lmodern"
    "geometry"
    "amsmath"
    "amssymb"
    "amsthm"
    "mathtools"
    "fancyhdr"
    "hyperref")
   (TeX-add-symbols
    '("eulerproblem" 2)
    "N"
    "Z"
    "Q"
    "R"
    "C"))
 :latex)

