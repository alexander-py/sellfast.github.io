from django.shortcuts import render
from django.http import FileResponse
from pathlib import Path
def home(request):
    return render(request, "home.html")



def download_checklist(request):
    file_path = Path(__file__).resolve().parent.parent / "downloads" / "exit_handover_checklist.txt"
    return FileResponse(
        open(file_path, "rb"),
        as_attachment=True,
        filename="exit_handover_checklist.txt",
    )