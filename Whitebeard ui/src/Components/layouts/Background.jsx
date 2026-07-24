import { useEffect, useRef } from "react";

function TopologyBackground() {
  const ref = useRef(null);
  const effectRef = useRef(null);

  useEffect(() => {
    if (!effectRef.current && window.VANTA && window.THREE) {
      effectRef.current = window.VANTA.TOPOLOGY({
        el: ref.current,
        mouseControls: true,
        touchControls: true,
        gyroControls: true,
        scale: 2.0,
        scaleMobile: 2.0,
        color: 0x35354b,
        backgroundColor: 0x101414,
      });
    }

    // 🔥 Fix: trigger resize on scroll
    const handleScroll = () => {
      if (effectRef.current) {
        effectRef.current.resize();
      }
    };

    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);

      if (effectRef.current) {
        try {
          effectRef.current.destroy();
        } catch (e) {}
        effectRef.current = null;
      }
    };
  }, []);

  return (
    <div
      ref={ref}
      style={{
        position: "fixed",
        inset: 0,
        zIndex: -1,
      }}
    />
  );
}

export default TopologyBackground;
