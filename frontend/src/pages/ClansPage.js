import React from 'react';
import { motion } from 'framer-motion';
import { Users, Trophy, Star, Shield } from 'lucide-react';

const ClansPage = () => {
  return (
    <div className="min-h-screen py-8">
      <motion.div 
        initial={{ opacity: 0, y: 20 }} 
        animate={{ opacity: 1, y: 0 }} 
        transition={{ duration: 0.6 }}
        className="text-center mb-12"
      >
        <h1 className="text-4xl font-bold mb-4 bg-gradient-to-r from-yellow-400 via-orange-500 to-red-500 bg-clip-text text-transparent">
          Star Regiment Clans
        </h1>
        <p className="text-xl text-gray-300 max-w-2xl mx-auto">
          Join Telugu movie fan armies and battle for supremacy in the trading arena!
        </p>
      </motion.div>

      <div className="trading-card max-w-4xl mx-auto text-center">
        <Users className="w-16 h-16 text-blue-400 mx-auto mb-4" />
        <h2 className="text-2xl font-bold mb-4">Fan Army Clans Coming Soon</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8">
          <div className="text-center">
            <Star className="w-12 h-12 text-yellow-400 mx-auto mb-3" />
            <h3 className="font-semibold mb-2">Star Regiments</h3>
            <p className="text-gray-400 text-sm">Join Chiranjeevi, Pawan Kalyan, and other star armies</p>
          </div>
          <div className="text-center">
            <Trophy className="w-12 h-12 text-green-400 mx-auto mb-3" />
            <h3 className="font-semibold mb-2">Clan Battles</h3>
            <p className="text-gray-400 text-sm">Compete for real-world perks and bragging rights</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ClansPage; 