import React from 'react';
import './Contacts.css';

const Contacts = () => {
  return (
    <div className="contact-field" id="contacts">
      <h2>Контакты</h2>
      <div className="contact-info">
        <div className="contact-item">
          <i className="icon-phone"></i>
          {/* <i src="/telephone.jpg"/> */}
          <p>+7 123 456 7890</p>
        </div>
        <div className="contact-item">
          <i className="icon-email"></i>
          {/* <i src="/mail_icon.png"/> */}
          <p>info@cardiogenetics.ru</p>
        </div>
        <div className="contact-item">
          <i className="icon-location"></i>
          {/* <i src="/geo_pos.jpg"/> */}
          <p>Russian Federation</p>
        </div>
      </div>
    </div>
  );
};

export default Contacts;
