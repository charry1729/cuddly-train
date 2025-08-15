import React from 'react';
import { motion } from 'framer-motion';
import { TrendingUp, BarChart3, Target } from 'lucide-react';

const TradingPage = () => {
  return (
    <div className="min-h-screen py-8">
      <motion.div 
        initial={{ opacity: 0, y: 20 }} 
        animate={{ opacity: 1, y: 0 }} 
        transition={{ duration: 0.6 }}
        className="text-center mb-12"
      >
        <h1 className="text-4xl font-bold mb-4 bg-gradient-to-r from-yellow-400 via-orange-500 to-red-500 bg-clip-text text-transparent">
          Trading Dashboard
        </h1>
        <p className="text-xl text-gray-300 max-w-2xl mx-auto">
          Coming Soon! Advanced trading features, real-time charts, and portfolio management.
        </p>
      </motion.div>

      <div className="trading-card max-w-4xl mx-auto text-center">
        <TrendingUp className="w-16 h-16 text-blue-400 mx-auto mb-4" />
        <h2 className="text-2xl font-bold mb-4">Trading Features Coming Soon</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
          <div className="text-center">
            <BarChart3 className="w-12 h-12 text-green-400 mx-auto mb-3" />
            <h3 className="font-semibold mb-2">Real-time Charts</h3>
            <p className="text-gray-400 text-sm">Live price updates and technical analysis</p>
          </div>
          <div className="text-center">
            <Target className="w-12 h-12 text-orange-400 mx-auto mb-3" />
            <h3 className="font-semibold mb-2">Portfolio Management</h3>
            <p className="text-gray-400 text-sm">Track your investments and performance</p>
          </div>
          <div className="text-center">
            <TrendingUp className="w-12 h-12 text-red-400 mx-auto mb-3" />
            <h3 className="font-semibold mb-2">Advanced Orders</h3>
            <p className="text-gray-400 text-sm">Limit orders, stop losses, and more</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TradingPage; 