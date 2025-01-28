import "./Organisations.css";
import React, { useEffect, useState } from "react";
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
            <a href={organisation.link} ><img src={organisation.image}/></a>
          </div>
        ))}
      </div>
      <Footer />
    </div>
  );
};

export default Organisations;