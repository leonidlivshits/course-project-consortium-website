// import logo from './logo.svg';
// import './App.css';
import React from 'react';
import Navbar from './components/Navbar/Navbar';
import Footer from './components/Footer/Footer';
import Contacts from './components/Contacts/Contacts';
import ContactForm from './components/ContactForm/ContactForm';

function App() {
  return (
    <div className="App">
      <Navbar />
      <div className="content">
        <h1>Добро пожаловать на сайт</h1>
        <p>Это консорциум по кардиогенетике</p>
      </div>
      <Contacts/>
      <ContactForm/>
      <Footer/>
    </div>
  );
}

export default App;
