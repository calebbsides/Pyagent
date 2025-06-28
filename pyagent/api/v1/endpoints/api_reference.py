from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/api-reference", response_class=HTMLResponse)
async def api_reference():
    html_content = """
    <html>
        <head>
            <title>API Reference</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Inter', Arial, sans-serif;
                    background: #f8fafc;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    max-width: 700px;
                    margin: 3em auto;
                    background: #fff;
                    border-radius: 16px;
                    box-shadow: 0 4px 24px rgba(44,62,80,0.08);
                    padding: 2.5em 2em 2em 2em;
                }
                h1 {
                    color: #2563eb;
                    font-size: 2.2em;
                    margin-bottom: 0.2em;
                    font-weight: 700;
                }
                h2 {
                    color: #334155;
                    margin-top: 2em;
                    font-size: 1.3em;
                    font-weight: 600;
                }
                ul {
                    list-style: none;
                    padding: 0;
                }
                li {
                    background: #f1f5f9;
                    margin-bottom: 1em;
                    border-radius: 8px;
                    padding: 1em 1.2em;
                    box-shadow: 0 1px 2px rgba(0,0,0,0.02);
                }
                strong {
                    color: #0f172a;
                    font-weight: 600;
                }
                code {
                    background: #e0e7ef;
                    padding: 2px 6px;
                    border-radius: 4px;
                    font-size: 1em;
                }
                pre {
                    background: #e0e7ef;
                    padding: 1em;
                    border-radius: 8px;
                    overflow-x: auto;
                    font-size: 1em;
                }
                .footer {
                    margin-top: 2.5em;
                    color: #64748b;
                    font-size: 0.98em;
                    text-align: center;
                }
                @media (max-width: 600px) {
                    .container { padding: 1em; }
                    h1 { font-size: 1.3em; }
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Pyagent API Reference</h1>
                <h2>Endpoints</h2>
                <ul>
                    <li><strong>GET /</strong><br>
                        <span style="color:#64748b">Returns a health check message.</span>
                    </li>
                    <li><strong>GET /v1/weather</strong><br>
                        <span style="color:#64748b">Returns weather information.</span>
                    </li>
                    <li><strong>GET /v1/api-reference</strong><br>
                        <span style="color:#64748b">This documentation page.</span>
                    </li>
                </ul>
                <h2>Usage</h2>
                <ul>
                <li>
                    <code>curl http://127.0.0.1:8000/</code>
                    </li>
                <li>
                    <code>curl http://127.0.0.1:8000/v1/weather</code>
                    </li>
                </ul>
                <div class="footer">
                    For more details, see the <code>ADDING_ENDPOINTS.md</code> file.
                </div>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
