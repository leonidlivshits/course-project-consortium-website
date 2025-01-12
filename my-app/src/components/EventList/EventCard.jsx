import React from 'react';
import { useNavigate } from 'react-router-dom';
import './EventList.css';

const EventCard = ({ event }) => {
  const navigate = useNavigate();

  const handleCardClick = () => {
    navigate(`/event/${event.id}`, { state: event });
  };

  return (
    <div className="col-lg-4 event-card" onClick={handleCardClick}>
      <div className="event-image">
        <img src={event.image} alt={event.title} />
      </div>
      <div className="event-content">
        <h3>{event.title}</h3>
        <p>{event.date}</p>
        <p>{event.description.substring(0, 100)}...</p>
      </div>
    </div>
  );
};

export default EventCard;
