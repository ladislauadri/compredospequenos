import axios from "axios";

// Pode ser algum servidor executando localmente: 
// http://localhost:3000

const api = axios.create({
  baseURL: "https://api.condominiosevizinhanca.com.br/api/v1",
});

export default api;