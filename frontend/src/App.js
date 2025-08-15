import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from 'react-query';
import { motion, AnimatePresence } from 'framer-motion';

// Components
import Navbar from './components/Navbar';
import Footer from './components/Footer';

// Pages
import HomePage from './pages/HomePage';
import MoviesPage from './pages/MoviesPage';
import TradingPage from './pages/TradingPage';
import ClansPage from './pages/ClansPage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';

// Context
import { AuthProvider } from './contexts/AuthContext';
import { TradingProvider } from './contexts/TradingContext';

// Create a client
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: 1,
      refetchOnWindowFocus: false,
    },
  },
});

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <AuthProvider>
        <TradingProvider>
          <Router>
            <div className="min-h-screen bg-gradient-to-br from-gray-900 via-blue-900 to-gray-900 text-white">
              <Navbar />
              
              <main className="container mx-auto px-4 py-8">
                <AnimatePresence mode="wait">
                  <Routes>
                    <Route 
                      path="/" 
                      element={
                        <motion.div
                          initial={{ opacity: 0, y: 20 }}
                          animate={{ opacity: 1, y: 0 }}
                          exit={{ opacity: 0, y: -20 }}
                          transition={{ duration: 0.3 }}
                        >
                          <HomePage />
                        </motion.div>
                      } 
                    />
                    
                    <Route 
                      path="/movies" 
                      element={
                        <motion.div
                          initial={{ opacity: 0, y: 20 }}
                          animate={{ opacity: 1, y: 0 }}
                          exit={{ opacity: 0, y: -20 }}
                          transition={{ duration: 0.3 }}
                        >
                          <MoviesPage />
                        </motion.div>
                      } 
                    />
                    
                    <Route 
                      path="/trading" 
                      element={
                        <motion.div
                          initial={{ opacity: 0, y: 20 }}
                          animate={{ opacity: 1, y: 0 }}
                          exit={{ opacity: 0, y: -20 }}
                          transition={{ duration: 0.3 }}
                        >
                          <TradingPage />
                        </motion.div>
                      } 
                    />
                    
                    <Route 
                      path="/clans" 
                      element={
                        <motion.div
                          initial={{ opacity: 0, y: 20 }}
                          animate={{ opacity: 1, y: 0 }}
                          exit={{ opacity: 0, y: -20 }}
                          transition={{ duration: 0.3 }}
                        >
                          <ClansPage />
                        </motion.div>
                      } 
                    />
                    
                    <Route 
                      path="/login" 
                      element={
                        <motion.div
                          initial={{ opacity: 0, y: 20 }}
                          animate={{ opacity: 1, y: 0 }}
                          exit={{ opacity: 0, y: -20 }}
                          transition={{ duration: 0.3 }}
                        >
                          <LoginPage />
                        </motion.div>
                      } 
                    />
                    
                    <Route 
                      path="/register" 
                      element={
                        <motion.div
                          initial={{ opacity: 0, y: 20 }}
                          animate={{ opacity: 1, y: 0 }}
                          exit={{ opacity: 0, y: -20 }}
                          transition={{ duration: 0.3 }}
                        >
                          <RegisterPage />
                        </motion.div>
                      } 
                    />
                  </Routes>
                </AnimatePresence>
              </main>
              
              <Footer />
            </div>
          </Router>
        </TradingProvider>
      </AuthProvider>
    </QueryClientProvider>
  );
}

export default App; 