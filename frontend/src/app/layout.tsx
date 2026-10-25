import React from 'react';
import Sidebar from '@/components/Sidebar';
import './globals.css';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-background text-foreground antialiased">
        <div className="flex min-h-screen">
          <Sidebar />
          <main className="flex-1 relative overflow-x-hidden">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}
