from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from .utils import getAllNotes, createNote, getNoteDetail, updateNote, deleteNote

# get all notes
@api_view(['GET', 'POST'])
def getNotes(request):
    if request.method  == 'GET': 
        return getAllNotes(request)

    if request.method  == 'POST': 
        return createNote(request)


# single note operations
@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):

    # gets a single note via note ID
    if request.method == 'GET':
        return getNoteDetail(request, pk)

    # updates a specific note
    if request.method == 'PUT':
        return updateNote(request, pk)

    # deletes a specific note
    if request.method == 'DELETE':
        return deleteNote(request, pk)