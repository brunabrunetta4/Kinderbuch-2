import subprocess
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

def render_pdf(html_rel, pdf_rel):
    pdf_abs = os.path.join(dir_path, pdf_rel)
    # Use the junction c:\Projekt\Kinderbuch-2 to avoid the '#' issue
    url = f"file:///c:/Projekt/Kinderbuch-2/{html_rel}"
    
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_abs}",
        url
    ]
    print(f"Rendering {html_rel} -> {pdf_rel}...")
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if os.path.exists(pdf_abs) and os.path.getsize(pdf_abs) > 0:
        print(f"Success! {pdf_rel} created ({os.path.getsize(pdf_abs)} bytes)")
    else:
        print(f"Failed to create {pdf_rel}! Returncode: {res.returncode}, Stderr: {res.stderr}")

if __name__ == '__main__':
    render_pdf("epubli_cover_17x24.html", "epubli_hardcover_17x24.pdf")
    render_pdf("epubli_druckvorlage_17x24.html", "epubli_buchblock_17x24.pdf")
