import React, { createContext, useContext, useState } from 'react';

const TradingContext = createContext();

export const useTrading = () => {
  const context = useContext(TradingContext);
  if (!context) {
    throw new Error('useTrading must be used within a TradingProvider');
  }
  return context;
};

export const TradingProvider = ({ children }) => {
  const [portfolio, setPortfolio] = useState([]);
  const [balance, setBalance] = useState(10000.0);

  const buyStock = (movieId, shares, price) => {
    const cost = shares * price;
    if (cost > balance) {
      throw new Error('Insufficient balance');
    }
    
    setBalance(prev => prev - cost);
    
    const existingPosition = portfolio.find(p => p.movieId === movieId);
    if (existingPosition) {
      setPortfolio(prev => prev.map(p => 
        p.movieId === movieId 
          ? { ...p, shares: p.shares + shares, avgPrice: ((p.avgPrice * p.shares) + cost) / (p.shares + shares) }
          : p
      ));
    } else {
      setPortfolio(prev => [...prev, { movieId, shares, avgPrice: price }]);
    }
  };

  const sellStock = (movieId, shares, price) => {
    const existingPosition = portfolio.find(p => p.movieId === movieId);
    if (!existingPosition || existingPosition.shares < shares) {
      throw new Error('Insufficient shares');
    }
    
    const revenue = shares * price;
    setBalance(prev => prev + revenue);
    
    if (existingPosition.shares === shares) {
      setPortfolio(prev => prev.filter(p => p.movieId !== movieId));
    } else {
      setPortfolio(prev => prev.map(p => 
        p.movieId === movieId 
          ? { ...p, shares: p.shares - shares }
          : p
      ));
    }
  };

  const value = {
    portfolio,
    balance,
    buyStock,
    sellStock,
  };

  return (
    <TradingContext.Provider value={value}>
      {children}
    </TradingContext.Provider>
  );
}; 