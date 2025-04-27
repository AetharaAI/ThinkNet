"use client";
import { useEffect } from "react";

export default function GalaxyBackground() {
  useEffect(() => {
    const canvas = document.getElementById("galaxy") as HTMLCanvasElement;
    const ctx = canvas?.getContext("2d");

    if (!canvas || !ctx) return;

    const stars = Array.from({ length: 100 }, () => ({
      x: Math.random() * window.innerWidth,
      y: Math.random() * window.innerHeight,
      radius: Math.random() * 1.5,
      velocity: Math.random() * 0.5,
    }));

    function draw() {
      ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);
      ctx.fillStyle = "#ffffff";
      stars.forEach((star) => {
        ctx.beginPath();
        ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
        ctx.fill();
        star.y += star.velocity;
        if (star.y > window.innerHeight) {
          star.y = 0;
          star.x = Math.random() * window.innerWidth;
        }
      });
      requestAnimationFrame(draw);
    }

    draw();
  }, []);

  return (
    <canvas
      id="galaxy"
      className="fixed top-0 left-0 w-full h-full z-0 opacity-30 pointer-events-none"
    ></canvas>
  );
}
