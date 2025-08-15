import React from 'react';
import { motion } from 'framer-motion';
import { TrendingUp, Calendar, Star, Users } from 'lucide-react';

const MoviesPage = () => {
  const movies = [
    {
      id: "1",
      title: "RRR",
      telugu_title: "ఆర్‌ఆర్‌ఆర్",
      contract_symbol: "RRR",
      current_price: 450.0,
      hype_score: 95.0,
      status: "released",
      genre: ["Action", "Drama", "Historical"],
      director: "S.S. Rajamouli",
      star_actor: "N.T. Rama Rao Jr.",
      heroine: "Alia Bhatt"
    },
    {
      id: "2", 
      title: "Pushpa: The Rise",
      telugu_title: "పుష్ప: ది రైజ్",
      contract_symbol: "PUSHPA",
      current_price: 320.0,
      hype_score: 88.0,
      status: "released",
      genre: ["Action", "Crime", "Drama"],
      director: "Sukumar",
      star_actor: "Allu Arjun",
      heroine: "Rashmika Mandanna"
    },
    {
      id: "3",
      title: "Salaar",
      telugu_title: "సలార్", 
      contract_symbol: "SALAAR",
      current_price: 180.0,
      hype_score: 92.0,
      status: "in_production",
      genre: ["Action", "Thriller"],
      director: "Prashanth Neel",
      star_actor: "Prabhas",
      heroine: "Shruti Haasan"
    }
  ];

  const getStatusColor = (status) => {
    switch (status) {
      case 'released': return 'text-green-400';
      case 'in_production': return 'text-yellow-400';
      case 'post_production': return 'text-blue-400';
      default: return 'text-gray-400';
    }
  };

  const getStatusText = (status) => {
    switch (status) {
      case 'released': return 'Released';
      case 'in_production': return 'In Production';
      case 'post_production': return 'Post Production';
      default: return status;
    }
  };

  return (
    <div className="min-h-screen py-8">
      {/* Header */}
      <motion.div 
        initial={{ opacity: 0, y: 20 }} 
        animate={{ opacity: 1, y: 0 }} 
        transition={{ duration: 0.6 }}
        className="text-center mb-12"
      >
        <h1 className="text-4xl font-bold mb-4 bg-gradient-to-r from-yellow-400 via-orange-500 to-red-500 bg-clip-text text-transparent">
          Movie Contracts
        </h1>
        <p className="text-xl text-gray-300 max-w-2xl mx-auto">
          Trade virtual stocks of your favorite Telugu movies. Research, predict, and profit from the hype!
        </p>
      </motion.div>

      {/* Movies Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {movies.map((movie, index) => (
          <motion.div
            key={movie.id}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: index * 0.1 }}
            className="movie-card group cursor-pointer"
          >
            {/* Movie Header */}
            <div className="mb-4">
              <div className="flex items-start justify-between mb-2">
                <h3 className="text-xl font-bold text-white">{movie.title}</h3>
                <span className={`px-2 py-1 rounded-full text-xs font-medium ${getStatusColor(movie.status)}`}>
                  {getStatusText(movie.status)}
                </span>
              </div>
              {movie.telugu_title && (
                <p className="text-lg text-blue-400 telugu-font">{movie.telugu_title}</p>
              )}
              <p className="text-sm text-gray-400">{movie.genre.join(' • ')}</p>
            </div>

            {/* Trading Info */}
            <div className="space-y-3 mb-4">
              <div className="flex items-center justify-between">
                <span className="text-gray-400">Contract Symbol:</span>
                <span className="font-mono text-lg font-bold text-green-400">{movie.contract_symbol}</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-gray-400">Current Price:</span>
                <span className="text-2xl font-bold text-white">₹{movie.current_price}</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-gray-400">Hype Score:</span>
                <div className="flex items-center space-x-2">
                  <div className="w-20 bg-gray-700 rounded-full h-2">
                    <div 
                      className="bg-gradient-to-r from-yellow-400 to-red-500 h-2 rounded-full" 
                      style={{ width: `${movie.hype_score}%` }}
                    ></div>
                  </div>
                  <span className="text-white font-semibold">{movie.hype_score}%</span>
                </div>
              </div>
            </div>

            {/* Movie Details */}
            <div className="space-y-2 text-sm text-gray-400">
              <div className="flex items-center space-x-2">
                <Calendar className="w-4 h-4" />
                <span>Director: {movie.director}</span>
              </div>
              <div className="flex items-center space-x-2">
                <Star className="w-4 h-4" />
                <span>Star: {movie.star_actor}</span>
              </div>
              <div className="flex items-center space-x-2">
                <Users className="w-4 h-4" />
                <span>Heroine: {movie.heroine}</span>
              </div>
            </div>

            {/* Action Buttons */}
            <div className="mt-6 flex space-x-3">
              <button className="btn-primary flex-1">
                <TrendingUp className="w-4 h-4 mr-2" />
                Trade Now
              </button>
              <button className="px-4 py-3 border border-gray-600 text-gray-300 rounded-lg hover:border-blue-500 hover:text-blue-400 transition-colors">
                Details
              </button>
            </div>
          </motion.div>
        ))}
      </div>

      {/* Call to Action */}
      <motion.div 
        initial={{ opacity: 0, y: 20 }} 
        animate={{ opacity: 1, y: 0 }} 
        transition={{ duration: 0.6, delay: 0.4 }}
        className="text-center mt-16"
      >
        <div className="trading-card max-w-2xl mx-auto">
          <h3 className="text-2xl font-bold mb-4">Ready to Start Trading?</h3>
          <p className="text-gray-300 mb-6">
            Join thousands of Telugu movie fans who are already trading virtual stocks. 
            Research, predict, and profit from the hype!
          </p>
          <button className="btn-primary">
            Create Account & Start Trading
          </button>
        </div>
      </motion.div>
    </div>
  );
};

export default MoviesPage; 