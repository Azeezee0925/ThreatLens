import api from "./api";

export async function getCharts() {
  const response = await api.get("/dashboard/charts");
  return response.data;
}