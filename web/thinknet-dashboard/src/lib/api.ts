// src/lib/api.ts

import axios from "axios";

const BASE_URL = "http://localhost:8000"; // ThinkNet Core

export const askThinkNet = async (prompt: string) => {
  try {
    const response = await axios.post(`${BASE_URL}/ask`, {
      prompt,
    });
    return response.data.response;
  } catch (error) {
    console.error("Error contacting ThinkNet Core:", error);
    throw new Error("Failed to connect to ThinkNet Core");
  }
};
