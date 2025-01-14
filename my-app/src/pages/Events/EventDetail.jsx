import React from 'react';
import { useLocation } from 'react-router-dom';
import ContactForm from '../../components/ContactForm/ContactForm';
import './EventDetail.css';
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";

const EventDetail = () => {
  const location = useLocation();
  const event = location.state;

  return (
    <section className="event-detail">
      <Navbar />
      <div className="container">
        <h2>{event.title}</h2>
        <p><strong>Дата:</strong> {event.date}</p>
        <p><strong>Время:</strong> {event.time}</p>
        <p><strong>Место проведения:</strong> {event.location}</p>
        <p>{event.description}</p>
        <ContactForm />
      </div>
      <Footer />
    </section>
  );
};

export default EventDetail;
