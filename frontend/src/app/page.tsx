import React from 'react';
import { Sparkles, ArrowRight, Clock, LayoutGrid } from 'lucide-react';
import Link from 'next/link';

export default function HomePage() {
  return (
    <div className="p-8 max-w-7xl mx-auto space-y-12">
      {/* Hero Section */}
      <section className="relative py-20 text-center space-y-6">
        <div className="absolute inset-0 -z-10 bg-cinematic-gradient opacity-50 rounded-full blur-3xl" />
        <h1 className="text-6xl font-bold tracking-tighter text-foreground">
          Unleash Your <span className="text-accent-highlight">Creativity</span>
        </h1>
        <p className="text-xl text-accent-muted max-w-2xl mx-auto leading-relaxed">
          Striker2.1 is a professional AI studio for high-fidelity image and video generation.
          Experience cinematic precision and absolute control over your vision.
        </p>
        <div className="flex items-center justify-center gap-4 pt-4">
          <Link
            href="/create/image"
            className="bg-accent text-dark-900 px-6 py-3 rounded-full font-semibold hover:bg-white transition-all flex items-center gap-2"
          >
            Start Creating <ArrowRight className="w-4 h-4" />
          </Link>
          <Link
            href="/docs"
            className="px-6 py-3 rounded-full font-semibold border border-dark-700 hover:bg-dark-800 transition-all"
          >
            Explore Guides
          </Link>
        </div >
      </section>

      {/* Quick Start Prompt */}
      <section className="bg-dark-800 border border-dark-700 rounded-2xl p-8 space-y-6">
        <div className="flex items-center gap-2 text-accent-highlight font-medium uppercase text-xs tracking-widest">
          <Sparkles className="w-4 h-4" />
          <span>Quick Start</span>
        </div>
        <div className="flex flex-col md:flex-row gap-4">
          <div className="flex-1 relative">
            <textarea
              placeholder="Describe your vision..."
              className="w-full h-24 bg-dark-900 border border-dark-700 rounded-xl p-4 text-foreground placeholder:text-accent-muted focus:outline-none focus:ring-2 focus:ring-accent-highlight transition-all resize-none"
            />
          </div >
          <div className="flex flex-col gap-2">
            <Link
              href="/create/image"
              className="bg-accent-highlight text-white px-6 py-3 rounded-xl font-semibold hover:opacity-90 transition-all text-center"
            >
              Generate Image
            </Link>
            <Link
              href="/create/video"
              className="bg-dark-700 text-accent px-6 py-3 rounded-xl font-semibold hover:bg-dark-600 transition-all text-center"
            >
              Generate Video
            </Link>
          </div >
        </div >
      </section>

      {/* Recent Projects */}
      <section className="space-y-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Clock className="w-5 h-5 text-accent-muted" />
            <h2 className="text-2xl font-semibold">Recent Projects</h2>
          </div >
          <Link href="/projects" className="text-sm text-accent-highlight hover:underline">View all</Link>
        </div >

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[1, 2, 3].map((i) => (
            <div key={i} className="group relative aspect-video bg-dark-800 border border-dark-700 rounded-xl overflow-hidden cursor-pointer hover:border-accent-highlight transition-all">
              <div className="absolute inset-0 bg-gradient-to-t from-dark-900 via-transparent to-transparent opacity-60" />
              <div className="absolute bottom-0 left-0 p-4 w-full">
                <p className="text-sm font-medium text-accent">Project {i}: Cinematic Landscape</p>
                <p className="text-xs text-accent-muted">Generated 2 days ago</p>
              </div >
              <div className="absolute top-3 right-3 opacity-0 group-hover:opacity-100 transition-opacity">
                <LayoutGrid className="w-4 h-4 text-accent" />
              </div >
            </div >
          ))}
        </div >
      </section>
    </div >
  );
}
