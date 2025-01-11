import React from "react";
import "./Organisations.css";

const AboutUs = () => {
  return (
    <div className="aboutUs">
      <h1>Члены консорциума</h1>
      <div className="team">
        <div className="teamMember">
          {/* <img src={leonidImage} alt="leo-livshits" /> */}
          <h2>
            Леонид
            <br />
            Лившиц
          </h2>
          <p>SE FCS HSE</p>
          <p>frontend</p>
          <a href="https://t.me/vyshkochka">Telegram</a>
        </div>
        <div className="teamMember">
          {/* <img src={dmitriyImage} alt="dima-alekseev" /> */}
          <h2>
            Дмитрий
            <br />
            Алексеев
          </h2>
          <p>SE FCS HSE</p>
          <p>design</p>
          <a href="https://t.me/Mister_V_1">Telegram</a>
        </div>
        <div className="teamMember">
          {/* <img src={alexandrImage} alt="alex-vasyukov" /> */}
          <h2>
            Александр
            <br />
            Васюков
          </h2>
          <p>SE FCS HSE</p>
          <p>frontend, CTO</p>
          <a href="https://t.me/overmindv">Telegram</a>
        </div>
        <div className="teamMember">
          {/* <img src={agilImage} alt="agil-amirov" /> */}
          <h2>
            Агиль
            <br />
            Амиров
          </h2>
          <p>SE FCS HSE</p>
          <p>backend</p>
          <a href="https://t.me/amirovagil">Telegram</a>
        </div>
      </div>
    </div>
  );
};

export default AboutUs;
