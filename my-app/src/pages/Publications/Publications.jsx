// const Publications = () => <div className="content"><h1>Публикации</h1></div>;
// export default Publications;

import React from "react";

import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";

const Publications = () => {
  return (
    <div>
      <Navbar />
      <div className="page"> 
      <h1>Публикации</h1>
      </div>
      <Footer />
    </div>
  );
};

export default Publications;