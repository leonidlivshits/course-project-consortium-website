import React from 'react';
import { useLocation } from 'react-router-dom';
import ContactForm from '../../components/ContactForm/ContactForm';
import './EventDetail.css';

const EventDetail = () => {
  const location = useLocation();
  const event = location.state;

  return (
    <section className="event-detail">
      <div className="container">
        <h2>{event.title}</h2>
        <p><strong>Дата:</strong> {event.date}</p>
        <p><strong>Время:</strong> {event.time}</p>
        <p><strong>Место проведения:</strong> {event.location}</p>
        <p>{event.description}</p>
        <ContactForm />
      </div>
    </section>
  );
};

export default EventDetail;
