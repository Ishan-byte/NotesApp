from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer


# get all notes
@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serialized_notes = NoteSerializer(notes, many = True)
    return Response(serialized_notes.data)


# gets a single note via note ID
@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id = pk)
    serialized_note = NoteSerializer(note, many = False)
    return Response(serialized_note.data)


# creates a new note
@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body = data['body']
    )
    serialized_note = NoteSerializer(note, many = False)
    return Response(serialized_note.data)


# updates a specific note
@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id = pk)
    serialized_note = NoteSerializer(instance=note, data = data)

    if serialized_note.is_valid():
        serialized_note.save()

    return Response(serialized_note.data)

# deletes a specific note
@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id =  pk)
    note.delete() 
    return Response("Note was Deleted!")