# Remove the file if it exists
Remove-Item -Path './_bibliography/web_papers.bib' -Force -ErrorAction SilentlyContinue

# Concatenate the contents of the files and append to web_papers.bib
Get-Content './bibliography/pubs_zhaw.bib', './bibliography/pubs_journal.bib', './bibliography/pubs_proc.bib', './bibliography/pubs_conf.bib', './bibliography/pubs_other.bib' | Set-Content './_bibliography/web_papers.bib'
