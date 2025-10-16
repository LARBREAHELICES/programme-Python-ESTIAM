# Programme Python E1, E2, E3, E4, E5

## Programme E1

## Programme E4


## Pratique

```bash
for f in *.html; do pandoc "$f" -o "pdf/${f%.html}.pdf" --pdf-engine=weasyprint; done

for f in *.md; do pandoc "$f" -o "pdf/${f%.md}.pdf" --pdf-engine=xelatex --standalone; done

```