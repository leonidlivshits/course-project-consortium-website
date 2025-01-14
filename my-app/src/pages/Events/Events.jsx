// import React from "react";
// import "./Events.css";
// import Navbar from "../../components/Navbar/Navbar";
// import Footer from "../../components/Footer/Footer";
// import { Link } from "react-router-dom";

// const events = [
//   {
//     id: "1",
//     title: "Конференция",
//     date: "15 января 2025",
//     location: "Москва, Россия",
//     time: "15:00",
//     description: "Присоединяйтесь к нашей ежегодной конференции по кардиогенетике!",
//   },
//   {
//     id: "2",
//     title: "Семинар",
//     date: "22 февраля 2025",
//     location: "Санкт-Петербург, Россия",
//     time: "15:00",
//     description: "Узнайте о последних методах в кардиогенетике на нашем семинаре.",
//   },
//   {
//     id: "3",
//     title: "Вебинар",
//     date: "10 марта 2025",
//     location: "Онлайн",
//     time: "15:00",
//     description: "Не пропустите наш вебинар о генетических тестах!",
//   },
// ];


// const Events = () => {
//   return (
//     <div className="page">
//       <Navbar />
//       <h1>События</h1>
//       <div className="events-list">
//         {events.map((event) => (
//           <div key={event.id} className="event">
//             <h2>{event.title}</h2>
//             <p>{event.description}</p>
//             <p><strong>Дата:</strong> {event.date}</p>
//             <p><strong>Время:</strong> {event.time}</p>
//             <p><strong>Место:</strong> {event.location}</p>
//             <Link to={`/events/${event.title}`} state={event} className="event-link">
//               Подробнее
//             </Link>
//           </div>
//         ))}
//       </div>
//       <Footer />
//     </div>
//   );
// };

// export default Events;

import React, { useEffect, useState } from "react";
import "./Events.css";
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";
import { Link } from "react-router-dom";

const Events = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/events')
      .then(response => response.json())
      .then(data => setEvents(data))
      .catch(error => console.error('Error fetching events:', error));
  }, []);

  return (
    <div className="page">
      <Navbar />
      <h1>События</h1>
      <div className="events-list">
        {events.map((event) => (
          <div key={event.id} className="event">
            <h2>{event.title}</h2>
            <p>{event.description}</p>
            <p><strong>Дата:</strong> {event.date}</p>
            <p><strong>Время:</strong> {event.time}</p>
            <p><strong>Место:</strong> {event.location}</p>
            <Link to={`/events/${event.title}`} state={event} className="event-link">
              Подробнее
            </Link>
          </div>
        ))}
      </div>
      <Footer />
    </div>
  );
};

export default Events;