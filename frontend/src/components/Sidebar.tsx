import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import {
  Home,
  Image as ImageIcon,
  Video,
  MoveRight,
  Edit3,
  FolderCanvas,
  Library,
  History,
  Settings
} from 'lucide-react';
import { clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

function cn(...inputs: any[]) {
  return twMerge(clsx(inputs));
}

const navItems = [
  { name: 'Home', href: '/', icon: Home },
  { name: 'Create Image', href: '/create/image', icon: ImageIcon },
  { name: 'Create Video', href: '/create/video', icon: Video },
  { name: 'Image to Video', href: '/create/i2v', icon: MoveRight },
  { name: 'Image Editor', href: '/editor', icon: Edit3 },
  { name: 'Projects', href: '/projects', icon: FolderCanvas },
  { name: 'Assets', href: '/assets', icon: Library },
  { name: 'History', href: '/history', icon: History },
  { name: 'Settings', href: '/settings', icon: Settings },
];

export default function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="w-64 h-screen sticky top-0 bg-dark-900 border-r border-dark-700 flex flex-col">
      <div className="p-6 flex items-center gap-3">
        <div className="w-8 h-8 bg-accent-highlight rounded-lg flex items-center justify-center font-bold text-dark-900">
          S
        </div>
        <span className="text-xl font-semibold tracking-tight">Striker2.1</span>
      </div>

      <nav className="flex-1 px-3 space-y-1">
        {navItems.map((item) => {
          const isActive = pathname === item.href;
          return (
            <Link
              key={item.name}
              href={item.href}
              className={cn(
                "flex items-center gap-3 px-3 py-2 rounded-md transition-colors text-sm font-medium",
                isActive
                  ? "bg-dark-700 text-accent"
                  : "text-accent-muted hover:bg-dark-800 hover:text-accent"
              )}
            >
              <item.icon className={cn("w-4 h-4", isActive ? "text-accent-highlight" : "text-accent-muted")} />
              {item.name}
            </Link>
          );
        })}
      </nav>

      <div className="p-4 border-t border-dark-700">
        <div className="bg-dark-800 rounded-lg p-3 text-xs text-accent-muted">
          <p className="font-medium text-accent mb-1">Pro Version</p>
          <p>Experimental build 2.1.0-alpha</p>
        </div>
      </div>
    </aside>
  );
}
