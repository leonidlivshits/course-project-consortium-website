import React from "react";
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";

const NoPage = () => {
  return (
    <div>
      <div>
        <Navbar />
      </div>
      <div className="page">
      </div>
      <div>
        <Footer />
      </div>
    </div>
  );
};

export default NoPage;
