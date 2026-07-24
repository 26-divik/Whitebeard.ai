import React from "react";
import { Link } from "react-router-dom";
import Typewriter from "typewriter-effect";
import { FaArrowCircleUp } from "react-icons/fa";
const MessageBar = () => {
  return (
    <>
      <div className="cursor-pointer min-w-3/4 flex items-center h-15 justify-between gap-4 px-5 border-2 border-tertiary text-tertiary text-nowrap tracking-widest rounded-4xl hover:opacity-90 transition-opacity">
      <div className=" w-1/2 flex items-center flex-row h-full lg:text-2xl text-xs">
        {" "}
        <Typewriter
          options={{
              strings: [
              "Guide me through this problem.",
              "Help me navigate this idea.",
              "Break this down for me.",
              "What’s the best way to approach this?",
              "Make this easier to understand.",
              "Show me how to do this properly.",
            ],
            autoStart: true,
            loop: true,
        }}
        />
        </div>
        <FaArrowCircleUp className="lg:text-4xl text-2xl h-15"/>
      </div>
    </>
  );
};
export default MessageBar;
