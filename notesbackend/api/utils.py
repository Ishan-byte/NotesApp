from .serializers import NoteSerializer
from .models import Note
from rest_framework.response import Response

# Notes
def getAllNotes(request):
    notes = Note.objects.all()
    serialized_notes = NoteSerializer(notes, many = True)
    return Response(serialized_notes.data)

# create Note
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body = data['body']
    )
    serialized_note = NoteSerializer(note, many = False)
    return Response(serialized_note.data)


# Note

# get Notes
def getNoteDetail(request, pk):
    note = Note.objects.get(id = pk)
    serialized_note = NoteSerializer(note, many = False)
    return Response(serialized_note.data)

# update Notes
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id = pk)
    serialized_note = NoteSerializer(instance=note, data = data)

    if serialized_note.is_valid():
        serialized_note.save()

    return Response(serialized_note.data)

# delete Note
def deleteNote(request, pk):
    note = Note.objects.get(id =  pk)
    note.delete() 
    return Response("Note was Deleted!")