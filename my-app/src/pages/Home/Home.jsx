import React from "react";

import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";
import ContactForm from "../../components/ContactForm/ContactForm";
import Contacts from "../../components/Contacts/Contacts"

const Home = () => {
  return (
    <div>
      <Navbar />
      <div className="page"> 
      <h1>Добро пожаловать на сайт</h1>
      </div>
      <Contacts/>
      <ContactForm/>
      <Footer />
    </div>
  );
};

export default Home;