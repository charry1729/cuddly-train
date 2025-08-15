import React from 'react';
import { Link } from 'react-router-dom';
import { Film, TrendingUp, Users, Trophy } from 'lucide-react';

const Navbar = () => {
  return (
    <nav className="bg-gray-900/80 backdrop-blur-lg border-b border-gray-700/50 sticky top-0 z-50">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center space-x-2">
            <div className="w-8 h-8 bg-gradient-to-r from-orange-500 to-red-500 rounded-lg flex items-center justify-center">
              <Film className="w-5 h-5 text-white" />
            </div>
            <span className="text-xl font-bold bg-gradient-to-r from-yellow-400 via-orange-500 to-red-500 bg-clip-text text-transparent">
              CineStox
            </span>
          </Link>

          {/* Navigation Links */}
          <div className="hidden md:flex items-center space-x-8">
            <Link to="/movies" className="text-gray-300 hover:text-white transition-colors flex items-center space-x-2">
              <TrendingUp className="w-4 h-4" />
              <span>Movies</span>
            </Link>
            <Link to="/trading" className="text-gray-300 hover:text-white transition-colors flex items-center space-x-2">
              <Trophy className="w-4 h-4" />
              <span>Trading</span>
            </Link>
            <Link to="/clans" className="text-gray-300 hover:text-white transition-colors flex items-center space-x-2">
              <Users className="w-4 h-4" />
              <span>Clans</span>
            </Link>
          </div>

          {/* Auth Buttons */}
          <div className="flex items-center space-x-4">
            <Link to="/login" className="text-gray-300 hover:text-white transition-colors">
              Login
            </Link>
            <Link to="/register" className="btn-primary">
              Get Started
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar; 