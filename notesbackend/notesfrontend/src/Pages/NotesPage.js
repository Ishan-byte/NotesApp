import React, { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { ReactComponent as LeftArrow } from '../Assets/arrow-left.svg'


const NotePage = ({ }) => {

    const params = useParams();
    const navigate = useNavigate();

    let noteid = params.id

    const [note, setNote] = useState(null)

    useEffect(() => {
        getNote();
    }, [noteid])


    let getNote = async () => {
        if (noteid === 'new') {
            return
        }
        let response = await fetch(`/api/note/${noteid}`)
        let data = await response.json()
        setNote(data)
    }

    let createNote = async () => {
        fetch(`/api/notes/create`, {
            method: "POST",
            headers: {
                "Content-type": "application/json"
            },
            body: JSON.stringify(note)
        })
        navigate('/')
    }

    let updateNote = async () => {
        fetch(`/api/note/${noteid}/update`, {
            method: "PUT",
            headers: {
                "Content-type": 'application/json'
            },
            body: JSON.stringify(note)
        })
        navigate('/')

    }

    let deleteNote = async () => {
        fetch(`/api/note/${noteid}/delete`, {
            method: 'DELETE',
            headers: {
                'Content-type': 'application/json'
            }
        })
        navigate('/')
    }


    let handleSubmit = () => {
        if (noteid !== 'new' && note.body == '') {
            deleteNote()
        } else if (noteid !== 'new') {
            updateNote();
        } else if (noteid == 'new' && note.body !== null) {
            createNote()
        }
    }


    let handleChange = (value) => {
        setNote({ ...note, 'body': value })
    }

    return (
        <div className='note'>
            <div className='note-header'>
                <h3>
                    <LeftArrow onClick={handleSubmit} />
                </h3>
                {noteid !== 'new' ? (
                    <button onClick={deleteNote}>Delete</button>
                ) : (
                    <button onClick={handleSubmit}>Done</button>
                )}
            </div>
            <textarea 
            onChange={(e) => (handleChange(e.target.value))}
            value={note?.body}></textarea>
        </div>
    )
}

export default NotePage