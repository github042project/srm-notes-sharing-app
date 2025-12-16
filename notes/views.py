from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note

def upload_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'upload.html', {'form': form})


def notes_list(request):
    semester = request.GET.get("semester")
    subject = request.GET.get("subject")

    notes = Note.objects.all()

    if semester:
        notes = notes.filter(semester=semester)
    if subject:
        notes = notes.filter(subject__icontains=subject)

    return render(request, 'notes_list.html', {"notes": notes})
