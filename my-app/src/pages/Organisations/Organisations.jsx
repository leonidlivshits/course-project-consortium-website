// import React from "react";
// import "./Organisations.css";

// const AboutUs = () => {
//   return (
//     <div className="aboutUs">
//       <h1>Члены консорциума</h1>
//       <div className="team">
//         <div className="teamMember">
//           {/* <img src={leonidImage} alt="leo-livshits" /> */}
//           <h2>
//             Леонид
//             <br />
//             Лившиц
//           </h2>
//           <p>SE FCS HSE</p>
//           <p>frontend</p>
//           <a href="https://t.me/vyshkochka">Telegram</a>
//         </div>
//         <div className="teamMember">
//           {/* <img src={dmitriyImage} alt="dima-alekseev" /> */}
//           <h2>
//             Дмитрий
//             <br />
//             Алексеев
//           </h2>
//           <p>SE FCS HSE</p>
//           <p>design</p>
//           <a href="https://t.me/Mister_V_1">Telegram</a>
//         </div>
//         <div className="teamMember">
//           {/* <img src={alexandrImage} alt="alex-vasyukov" /> */}
//           <h2>
//             Александр
//             <br />
//             Васюков
//           </h2>
//           <p>SE FCS HSE</p>
//           <p>frontend, CTO</p>
//           <a href="https://t.me/overmindv">Telegram</a>
//         </div>
//         <div className="teamMember">
//           {/* <img src={agilImage} alt="agil-amirov" /> */}
//           <h2>
//             Агиль
//             <br />
//             Амиров
//           </h2>
//           <p>SE FCS HSE</p>
//           <p>backend</p>
//           <a href="https://t.me/amirovagil">Telegram</a>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default AboutUs;

// import React from "react";
import "./Organisations.css";

import React, { useEffect, useState } from "react";
// import "./News.css";
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";

const Organisations = () => {
  const [organisations, setOrganisations] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/organisations')
      .then(response => response.json())
      .then(data => setOrganisations(data))
      .catch(error => console.error('Error fetching organisations:', error));
  }, []);

  return (
    <div className="aboutUs">
      <Navbar />
      <h1>Члены консорциума</h1>
      <div className="team">
        {organisations.map((organisation) => (
          <div key={organisation.id} className="teamMember">
            {/* <h2>{news.title}</h2> */}
            {/* <p><strong>Авторы:</strong> {news.authors}</p> */}
            <a href={organisation.link} ><img src={organisation.image}/></a>
          </div>
        ))}
      </div>
      <Footer />
    </div>
  );
};

export default Organisations;