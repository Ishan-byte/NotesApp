import React from 'react'
import { Link } from 'react-router-dom'


let getNoteTime = (note) => {
  return new Date(note.updated).toLocaleDateString()  
}

let getNotesTitle = ( note ) => { 
    let title  = note.body.split('\n')[0];
    if (title.length > 45) {
      title = title.slice(0, 45)
    }
    return title
}

const ListItem = ({ note }) => {

  return (
    <Link to={`/note/${note.id}`}>
      <div className='notes-list-item'>
        <h1>{getNotesTitle(note)}</h1>
        <p><span>{getNoteTime(note)}</span></p>
      </div>
    </Link>
  )
}

export default ListItem