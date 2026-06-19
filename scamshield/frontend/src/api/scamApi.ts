import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api";

export const analyzeMessage = async (message: string) => {
  const response = await axios.post(`${API_URL}/analyze`, {
    message,
  });

  return response.data;
};