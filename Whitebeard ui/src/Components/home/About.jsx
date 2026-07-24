import React from "react";

const About = () => {
  return (
    <>
      <div className="h-fit">
        <div className="flex flex-col items-center mb-30 gap-9 h-fit w-full font-bold text-primary font-work-sans tracking-widest">
          <h1 className="lg:text-6xl text-2xl">ABOUT</h1>
          <h1 className="lg:text-2xl text-xs text-start w-3/4 text-primary">
            Whitebeard AI is a conversational AI system inspired by the presence
            and authority of Whitebeard from One Piece. The aim is to create a
            system that feels structured and consistent rather than a simple
            prompt-response chatbot. It focuses on context-aware conversations
            where each interaction builds on previous ones, allowing users to
            experience a more continuous and meaningful dialogue. Users can
            create and manage chat sessions, enabling persistent conversations
            instead of isolated responses. The overall design reflects
            reliability and continuity, aligning with the core theme behind the
            name and inspiration.
          </h1>
          <h1 className="lg:text-2xl text-xs text-start w-3/4 text-primary">
            From a technical perspective, Whitebeard AI is built using a modular
            backend architecture with Flask and MongoDB. Chat sessions are
            stored as structured data, making it possible to maintain history
            and pass context during interactions. The API layer is designed
            around clear endpoints for chat creation, message handling, and
            retrieval, ensuring scalability and maintainability. It integrates
            with generative AI services to generate responses that consider both
            current input and prior conversation context. The system structure
            emphasizes clean separation of logic, making it easier to extend
            with additional features over time.
          </h1>
          <h1 className="lg:text-2xl text-xs text-start w-3/4 text-primary">
            The project is developed by Divik Goel and follows an open-source
            approach, allowing others to explore, use, and build upon it. The
            complete source code is available on GitHub at
            https://github.com/26-divik/Whitebeard.ai, where the backend
            structure and implementation details can be reviewed. More
            information about the developer and related work can be found on
            https://divikgoel.page, which serves as a central hub for projects
            and technical exploration. Going forward, the focus is on improving
            memory handling, enhancing personalization, and expanding
            capabilities while keeping the architecture clean and adaptable.
          </h1>
        </div>
      </div>
    </>
  );
};

export default About;
