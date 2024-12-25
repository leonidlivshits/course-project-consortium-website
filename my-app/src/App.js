// import logo from './logo.svg';
// import './App.css';
import React from 'react';
import Navbar from './components/Navbar/Navbar';

function App() {
  return (
    <div className="App">
      <Navbar />
      <div className="content">
        <h1>Добро пожаловать на сайт</h1>
        <p>Это консорциум по кардиогенетике</p>
      </div>
    </div>
  );
}

export default App;
