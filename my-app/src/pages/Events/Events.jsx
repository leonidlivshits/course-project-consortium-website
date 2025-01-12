import React from "react";
import "./Events.css";
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";
import { Link } from "react-router-dom";

const events = [
  {
    id: "1",
    title: "Конференция",
    date: "15 января 2025",
    location: "Москва, Россия",
    time: "15:00",
    description: "Присоединяйтесь к нашей ежегодной конференции по кардиогенетике!",
  },
  {
    id: "2",
    title: "Семинар",
    date: "22 февраля 2025",
    location: "Санкт-Петербург, Россия",
    time: "15:00",
    description: "Узнайте о последних методах в кардиогенетике на нашем семинаре.",
  },
  {
    id: "3",
    title: "Вебинар",
    date: "10 марта 2025",
    location: "Онлайн",
    time: "15:00",
    description: "Не пропустите наш вебинар о генетических тестах!",
  },
];

// const Events = () => {
//   return (
//     <div>
//       <Navbar />
//       <h1>События</h1>
//       <ul>
//         {events.map((event) => (
//           <li key={event.id}>
//             <Link to={`/events/${event.title}`} state={event}>
//               {event.title} - {event.date} - {event.time}
//             </Link>
//           </li>
//         ))}
//       </ul>
//       <Footer />
//     </div>
//   );
// };

// export default Events;

const Events = () => {
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

// const Events = () => {
//   return (
//     <div>
//       <Navbar />
//       <div className="page"> 
//       <h1>События</h1>
//       </div>
//       <EventList/>
//       <Footer />
//     </div>
//   );
// };

// export default Events;