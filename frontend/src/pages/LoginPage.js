import React from 'react';
import { motion } from 'framer-motion';
import { User, Lock, Film } from 'lucide-react';

const LoginPage = () => {
  return (
    <div className="min-h-screen py-8">
      <motion.div 
        initial={{ opacity: 0, y: 20 }} 
        animate={{ opacity: 1, y: 0 }} 
        transition={{ duration: 0.6 }}
        className="text-center mb-12"
      >
        <h1 className="text-4xl font-bold mb-4 bg-gradient-to-r from-yellow-400 via-orange-500 to-red-500 bg-clip-text text-transparent">
          Welcome Back
        </h1>
        <p className="text-xl text-gray-300 max-w-2xl mx-auto">
          Sign in to your CineStox account and continue your trading journey!
        </p>
      </motion.div>

      <div className="trading-card max-w-md mx-auto">
        <div className="text-center mb-6">
          <div className="w-16 h-16 bg-gradient-to-r from-orange-500 to-red-500 rounded-full flex items-center justify-center mx-auto mb-4">
            <Film className="w-8 h-8 text-white" />
          </div>
          <h2 className="text-2xl font-bold">Sign In</h2>
        </div>

        <form className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">Email</label>
            <div className="relative">
              <User className="w-5 h-5 text-gray-400 absolute left-3 top-3" />
              <input
                type="email"
                className="w-full pl-10 pr-4 py-3 bg-gray-800/50 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:border-blue-500 focus:outline-none"
                placeholder="Enter your email"
              />
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">Password</label>
            <div className="relative">
              <Lock className="w-5 h-5 text-gray-400 absolute left-3 top-3" />
              <input
                type="password"
                className="w-full pl-10 pr-4 py-3 bg-gray-800/50 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:border-blue-500 focus:outline-none"
                placeholder="Enter your password"
              />
            </div>
          </div>

          <button type="submit" className="btn-primary w-full">
            Sign In
          </button>
        </form>

        <div className="text-center mt-6">
          <p className="text-gray-400">
            Don't have an account?{' '}
            <a href="/register" className="text-blue-400 hover:text-blue-300">
              Sign up here
            </a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default LoginPage; 