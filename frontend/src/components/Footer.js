import React from 'react';
import { Film, Heart, Shield } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="bg-gray-900/80 border-t border-gray-700/50 mt-20">
      <div className="container mx-auto px-4 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Brand */}
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center space-x-2 mb-4">
              <div className="w-8 h-8 bg-gradient-to-r from-orange-500 to-red-500 rounded-lg flex items-center justify-center">
                <Film className="w-5 h-5 text-white" />
              </div>
              <span className="text-xl font-bold bg-gradient-to-r from-yellow-400 via-orange-500 to-red-500 bg-clip-text text-transparent">
                CineStox
              </span>
            </div>
            <p className="text-gray-400 mb-4">
              Where Film Fandom Meets Strategic Trading. Join the revolution of hype-driven movie stock trading!
            </p>
            <div className="flex items-center space-x-2 text-gray-500">
              <Heart className="w-4 h-4" />
              <span>Made with love for Telugu cinema</span>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="text-white font-semibold mb-4">Quick Links</h3>
            <ul className="space-y-2 text-gray-400">
              <li><a href="/movies" className="hover:text-white transition-colors">Movies</a></li>
              <li><a href="/trading" className="hover:text-white transition-colors">Trading</a></li>
              <li><a href="/clans" className="hover:text-white transition-colors">Clans</a></li>
              <li><a href="/leaderboard" className="hover:text-white transition-colors">Leaderboard</a></li>
            </ul>
          </div>

          {/* Legal */}
          <div>
            <h3 className="text-white font-semibold mb-4">Legal</h3>
            <ul className="space-y-2 text-gray-400">
              <li><a href="/terms" className="hover:text-white transition-colors">Terms of Service</a></li>
              <li><a href="/privacy" className="hover:text-white transition-colors">Privacy Policy</a></li>
              <li className="flex items-center space-x-2">
                <Shield className="w-4 h-4" />
                <span>Virtual Economy Only</span>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t border-gray-700/50 mt-8 pt-8 text-center text-gray-500">
          <p>&copy; 2024 CineStox. All rights reserved. This is a virtual trading platform with no real money involved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer; 