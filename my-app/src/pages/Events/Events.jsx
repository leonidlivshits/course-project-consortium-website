// const Events = () => <div className="content"><h1>События</h1></div>;
// export default Events;

import React from "react";

import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";

const Events = () => {
  return (
    <div>
      <Navbar />
      <div className="page"> 
      <h1>События</h1>
      </div>
      <Footer />
    </div>
  );
};

export default Events;