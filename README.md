# Web Application Security Assessment

Source reconstructed from `Final_Project. (2).pdf`.

## Included
- Flask application source documented in the report
- `templates/index.html`
- `templates/upload.html`
- `templates/command.html`
- `templates/xss.html`
- `Final_Project_Report.pdf`

## Security assessment scope
The report documents three vulnerabilities:
- unrestricted file upload
- OS command injection
- reflected XSS

## Reconstruction notes
The supplied report contains the backend code for `/`, `/upload`, and `/command`. It documents an `/xss` endpoint and provides `xss.html`, but the `app.py` source shown in the report does not include an `/xss` route. No undocumented backend code is silently added here.

The report also references visual assets under `static/`, but those assets were not available as standalone source files in the supplied report.
