import "./globals.css";
import type { Metadata } from "next";
import Sidebar from "@/components/layout/Sidebar";
import Navbar from "@/components/layout/Navbar";

export const metadata: Metadata = {
  title: "ThreatLens AI",
  description: "Enterprise Threat Intelligence Platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="bg-slate-950 text-white">

        <div className="flex">

          <Sidebar />

          <div className="flex-1">

            <Navbar />

            <main className="p-8">
              {children}
            </main>

          </div>

        </div>

      </body>
    </html>
  );
}