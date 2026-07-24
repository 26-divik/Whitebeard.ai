import React from "react";
import TopologyBackground from "./Background";
import Footer from "./Footer";
import { Outlet } from "react-router-dom";

const MainLayout = () => {
  return (
    <div style={{ position: "relative", minHeight: "100vh", overflowX: "hidden" }}>
      <TopologyBackground />

      <div style={{ position: "absolute", top: 0, width: "100%", zIndex:1}}>
        <div>
         <Outlet />
        </div>
        <Footer/>
      </div>
    </div>
  );
};

export default MainLayout;
