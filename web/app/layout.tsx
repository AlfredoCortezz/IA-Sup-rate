import type { Metadata } from "next";
import type { ReactNode } from "react";
import "./globals.css";
import { TutorChat } from "@/components/TutorChat";

/**
 * METADATOS: el título y la descripción que aparecen en la pestaña del
 * navegador y cuando compartes el link.
 *
 * 🚩 TODO (Semana 9): pon tu nombre y tu descripción.
 */
export const metadata: Metadata = {
  title: "Mi Portafolio de IA",
  description: "Proyectos de Inteligencia Artificial y Desarrollo Web — Semanas 9 y 10",
};

/**
 * LAYOUT = el "molde" que envuelve TODAS las páginas.
 * Aquí van cosas que se repiten siempre: el <html>, el <body>, fuentes, etc.
 */
export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="es">
      <body>
        {children}
        <TutorChat />
      </body>
    </html>
  );
}
