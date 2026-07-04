import api from "./api";

export async function downloadReport(ioc: string) {

    const response = await api.post(
        "/report",
        { ioc },
        {
            responseType: "blob",
        }
    );

    const url = window.URL.createObjectURL(
        new Blob([response.data])
    );

    const link = document.createElement("a");

    link.href = url;

    link.setAttribute(
        "download",
        `ThreatLens_Report_${ioc}.pdf`
    );

    document.body.appendChild(link);

    link.click();

    link.remove();
}