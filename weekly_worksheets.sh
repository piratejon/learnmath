#!/bin/bash

for op in add sub mul idiv rdiv; do
  for d in `seq 0 4`; do
    d=`date -d "+${d} days" +%F`
    case "${op}" in
      add|sub)
        cnt=20
        ;;
      *)
        cnt=12
        ;;
    esac

    python generate_worksheet.py out.tex "${op}" "${cnt}" 108
    pdflatex out
    mv out.pdf "${op}-${d}.pdf"
  done
done

