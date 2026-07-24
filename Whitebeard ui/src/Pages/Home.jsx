import React from "react";
import { motion } from "framer-motion";
import Hero from "../Components/home/Hero";
import About from "../Components/home/About";
const Home = () => {
  return (
    <>
      <motion.div className="w-full"
        initial={{ opacity: 0, scale: 0.95, y: 50 }}
        whileInView={{ opacity:1, scale: 1, y: 0 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
        viewport={{ once: true }}
        className="p-10"
      >
        <Hero/>
      </motion.div>
      <About />
    </>
  );
};

export default Home;
