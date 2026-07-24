import React from "react";
import logo from "../../assets/logo.svg";
import github from "../../assets/github.svg";
import { FaExternalLinkAlt } from "react-icons/fa";
import { Link, NavLink } from "react-router-dom";
const Footer = () => {
  return (
    <div className="flex flex-col lg:py-5 bg-tertiary/20 text-primary font-work-sans tracking-widest w-full">
      <div className="flex lg:flex-row flex-col w-full justify-around items-center gap-5 lg:mt-10 mt-3">
        <img
          className="lg:w-1/4 w-3/4 cursor-pointer"
          onClick={() => window.location.reload()}
          src={logo}
          alt="logo"
        />
        <div className="flex flex-row items-start lg:gap-35 gap-20">
          <div className="flex flex-col">
            <h1 className="w-fit cursor-pointer lg:text-3xl text-lg">
              NAVIGATION
            </h1>
            <div className="lg:text-xl text-xs text-start">
              <NavLink
                to="/"
                className={({ isActive }) =>
                  `w-fit cursor-pointer hover:opacity-80 ${
                    isActive ? "text-tertiary" : "hover:text-tertiary"
                  }`
                }
              >
                <h1>Introduction</h1>
              </NavLink>
              <NavLink
                to="/signup"
                className={({ isActive }) =>
                  `w-fit cursor-pointer hover:opacity-80 ${
                    isActive ? "text-tertiary" : "hover:text-tertiary"
                  }`
                }
              >
                <h1>Sign up</h1>
              </NavLink>

              <NavLink
                to="/login"
                className={({ isActive }) =>
                  `w-fit cursor-pointer hover:opacity-80 ${
                    isActive ? "text-tertiary" : "hover:text-tertiary"
                  }`
                }
              >
                <h1>Sign in</h1>
              </NavLink>
            </div>
          </div>
          <div className="flex flex-col">
            <h1 className="w-fit cursor-pointer lg:text-3xl text-lg">
              DEVELOPER
            </h1>
            <div className="lg:text-xl text-xs text-start">
              <h1 className="w-fit cursor-pointer">
                Divik Goel
              </h1>

              <Link to="http://divikgoel.page" target="_blank">
                <h1 className="w-fit cursor-pointer hover:text-tertiary hover:opacity-80">
                  Contact
                </h1>
              </Link>
            </div>
          </div>
        </div>
      </div>
      <div className="flex flex-col lg:flex-row justify-around w-full items-center lg:mt-15 mt-2 flex-nowrap">
        <Link to="https://github.com/26-divik/Whitebeard.ai" target="_blank">
          <h1 className="text-center lg:text-xl text-sm mt-5 cursor-pointer hover:text-tertiary hover:opacity-80 transition-colors">
            Source Code <FaExternalLinkAlt className="inline" />{" "}
          </h1>
        </Link>

        <h1 className="cursor-pointer text-center lg:text-xl text-sm mt-5">
          © 2026 Divik Goel. OPEN SOURCE PROJECT
        </h1>
      </div>
    </div>
  );
};

export default Footer;
