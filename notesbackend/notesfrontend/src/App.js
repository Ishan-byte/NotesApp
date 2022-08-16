//Css
import './App.css';

//Imports
import { HashRouter as Router, Routes, Route } from 'react-router-dom';

// Components
import Header from './Components/Header';
import Notes from './Pages/NotesListPage';
import NotePage from './Pages/NotesPage';

function App() {
  return (
    <div className="container dark">
      <div className='app'>
        <Router >
          <Header />
          <Routes>
            <Route path="/" exact element={<Notes />} />
            <Route path="/note/:id" exact element={<NotePage />} />
          </Routes>
        </Router>
      </div>
    </div>

  );
}

export default App;
