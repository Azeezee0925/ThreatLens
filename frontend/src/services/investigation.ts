import api from "./api";

export async function investigateIOC(ioc: string) {
  const response = await api.post("/investigate", {
    ioc: ioc,
  });

  return response.data;
}