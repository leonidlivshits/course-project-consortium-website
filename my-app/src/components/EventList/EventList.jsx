// import React from "react";
// import { Link } from "react-router-dom";
// import { EVENT_DETAIL_ROUTE } from "../../routes/Routes";

// const events = [
//   {
//     id: "1",
//     title: "Конференция",
//     date: "15 января 2025",
//     location: "Москва, Россия",
//     description: "Присоединяйтесь к нашей ежегодной конференции по кардиогенетике!",
//   },
//   {
//     id: "2",
//     title: "Семинар",
//     date: "22 февраля 2025",
//     location: "Санкт-Петербург, Россия",
//     description: "Узнайте о последних методах в кардиогенетике на нашем семинаре.",
//   },
//   {
//     id: "3",
//     title: "Вебинар",
//     date: "10 марта 2025",
//     location: "Онлайн",
//     description: "Не пропустите наш вебинар о генетических тестах!",
//   },
// ];

// const EventList = () => {
//   return (
//     <div>
//       <h1>События</h1>
//       <ul>
//         {events.map((event) => (
//           <li key={event.id}>
//             <Link to={`${EVENT_DETAIL_ROUTE.replace(":id", event.id)}`}>
//               {event.title} - {event.date}
//             </Link>
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// };

// export default EventList;
