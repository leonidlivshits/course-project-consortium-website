import React from 'react';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <a href="/" className="navbar-logo">
          <img src="/hse_logo.png"/>
          {/* <span>Кардиогенетика</span> */}
        </a>
        <div className="menu-toggle" id="mobile-menu">
          <span className="bar"></span>
          <span className="bar"></span>
          <span className="bar"></span>
        </div>
        <ul className="nav-menu">
          <li className="nav-item">
            <a href="/" className="nav-link">Главная</a>
          </li>
          <li className="nav-item">
            <a href="/organisations" className="nav-link">Организации</a>
          </li>
          <li className="nav-item">
            <a href="/publications" className="nav-link">Публикации</a>
          </li>
          <li className="nav-item">
            <a href="/news" className="nav-link">Новости</a>
          </li>
          <li className="nav-item">
            <a href="/projects" className="nav-link">Проекты</a>
          </li>
          <li className="nav-item">
            <a href="/events" className="nav-link">События</a>
          </li>
        </ul>
        <div className="nav-contact">
          <a href="/contacts" className="btn-contact">Контакты</a>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
