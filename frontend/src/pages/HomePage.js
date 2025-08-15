import React from 'react';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import { 
  TrendingUp, 
  Users, 
  Award, 
  Globe, 
  Zap, 
  Shield,
  Film,
  BarChart3,
  Star,
  Rocket
} from 'lucide-react';

const HomePage = () => {
  const features = [
    {
      icon: <TrendingUp className="w-8 h-8" />,
      title: "Hype-Driven Trading",
      description: "Trade virtual stocks based on movie hype, trailer reactions, and fan sentiment",
      color: "from-red-500 to-pink-500"
    },
    {
      icon: <Users className="w-8 h-8" />,
      title: "Telugu Fan Army",
      description: "Join star regiments, form clans, and boost your favorite movies together",
      color: "from-blue-500 to-cyan-500"
    },
    {
      icon: <Globe className="w-8 h-8" />,
      title: "Reddit Integration",
      description: "Convert r/tollywood posts into tradable contracts and sentiment data",
      color: "from-green-500 to-emerald-500"
    },
    {
      icon: <Award className="w-8 h-8" />,
      title: "Skill-Based Rewards",
      description: "Earn research points, mint NFTs, and climb the trading leaderboard",
      color: "from-yellow-500 to-orange-500"
    }
  ];

  const stats = [
    { label: "Active Movies", value: "25+", icon: <Film className="w-6 h-6" /> },
    { label: "Daily Traders", value: "10K+", icon: <Users className="w-6 h-6" /> },
    { label: "Fan Clans", value: "50+", icon: <Star className="w-6 h-6" /> },
    { label: "Success Rate", value: "85%", icon: <BarChart3 className="w-6 h-6" /> }
  ];

  const upcomingEvents = [
    {
      title: "Sankranthi Battle Royale",
      description: "Weekend-long trading competition with hourly liquidations",
      date: "Jan 15-17, 2024",
      status: "Coming Soon",
      color: "bg-gradient-to-r from-orange-500 to-red-500"
    },
    {
      title: "FDFS Frenzy",
      description: "First Day First Show hype zones with geo-tracking",
      date: "Every Friday",
      status: "Live",
      color: "bg-gradient-to-r from-green-500 to-blue-500"
    },
    {
      title: "Trailer Reaction Gambits",
      description: "Bet on trailer metrics and mint limited NFTs",
      date: "Ongoing",
      status: "Active",
      color: "bg-gradient-to-r from-purple-500 to-pink-500"
    }
  ];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="text-center py-20">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <h1 className="text-6xl font-bold mb-6 bg-gradient-to-r from-yellow-400 via-orange-500 to-red-500 bg-clip-text text-transparent">
            CineStox
          </h1>
          <p className="text-2xl mb-8 text-gray-300 max-w-3xl mx-auto">
            Where Film Fandom Meets Strategic Trading
          </p>
          <p className="text-lg mb-12 text-gray-400 max-w-2xl mx-auto">
            Trade virtual stocks of your favorite Telugu movies, join fan armies, and turn hype into profit. 
            Experience the world's first culturally-rooted movie trading platform.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              to="/register"
              className="px-8 py-4 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-lg hover:from-orange-600 hover:to-red-600 transition-all duration-300 transform hover:scale-105"
            >
              <Rocket className="inline-block w-5 h-5 mr-2" />
              Start Trading Now
            </Link>
            <Link
              to="/movies"
              className="px-8 py-4 border-2 border-blue-500 text-blue-400 font-semibold rounded-lg hover:bg-blue-500 hover:text-white transition-all duration-300"
            >
              <Film className="inline-block w-5 h-5 mr-2" />
              Browse Movies
            </Link>
          </div>
        </motion.div>
      </section>

      {/* Stats Section */}
      <section className="py-16">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="grid grid-cols-2 md:grid-cols-4 gap-8"
        >
          {stats.map((stat, index) => (
            <div key={index} className="text-center">
              <div className="flex justify-center mb-3 text-blue-400">
                {stat.icon}
              </div>
              <div className="text-3xl font-bold text-white mb-2">{stat.value}</div>
              <div className="text-gray-400">{stat.label}</div>
            </div>
          ))}
        </motion.div>
      </section>

      {/* Features Section */}
      <section className="py-16">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.4 }}
          className="text-center mb-16"
        >
          <h2 className="text-4xl font-bold mb-4">Why Choose CineStox?</h2>
          <p className="text-xl text-gray-400 max-w-2xl mx-auto">
            Experience the perfect blend of entertainment, community, and strategic trading
          </p>
        </motion.div>

        <div className="grid md:grid-cols-2 gap-8">
          {features.map((feature, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, x: index % 2 === 0 ? -30 : 30 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8, delay: 0.6 + index * 0.1 }}
              className="bg-gray-800/50 backdrop-blur-sm rounded-xl p-8 border border-gray-700 hover:border-gray-600 transition-all duration-300"
            >
              <div className={`inline-flex p-3 rounded-lg bg-gradient-to-r ${feature.color} mb-6`}>
                {feature.icon}
              </div>
              <h3 className="text-2xl font-bold mb-4">{feature.title}</h3>
              <p className="text-gray-400 leading-relaxed">{feature.description}</p>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Upcoming Events Section */}
      <section className="py-16">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.8 }}
          className="text-center mb-16"
        >
          <h2 className="text-4xl font-bold mb-4">Upcoming Events</h2>
          <p className="text-xl text-gray-400 max-w-2xl mx-auto">
            Don't miss these exciting trading opportunities and fan events
          </p>
        </motion.div>

        <div className="grid md:grid-cols-3 gap-8">
          {upcomingEvents.map((event, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 1.0 + index * 0.1 }}
              className="bg-gray-800/50 backdrop-blur-sm rounded-xl p-6 border border-gray-700 hover:border-gray-600 transition-all duration-300"
            >
              <div className={`inline-block px-3 py-1 rounded-full text-xs font-semibold text-white mb-4 ${event.color}`}>
                {event.status}
              </div>
              <h3 className="text-xl font-bold mb-3">{event.title}</h3>
              <p className="text-gray-400 text-sm mb-4">{event.description}</p>
              <div className="text-blue-400 text-sm font-medium">{event.date}</div>
            </motion.div>
          ))}
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 text-center">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 1.2 }}
        >
          <h2 className="text-4xl font-bold mb-6">Ready to Start Your Trading Journey?</h2>
          <p className="text-xl text-gray-400 mb-8 max-w-2xl mx-auto">
            Join thousands of Telugu movie fans who are already trading and earning on CineStox
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              to="/register"
              className="px-8 py-4 bg-gradient-to-r from-green-500 to-blue-500 text-white font-semibold rounded-lg hover:from-green-600 hover:to-blue-600 transition-all duration-300 transform hover:scale-105"
            >
              <Zap className="inline-block w-5 h-5 mr-2" />
              Get Started Free
            </Link>
            <Link
              to="/clans"
              className="px-8 py-4 border-2 border-purple-500 text-purple-400 font-semibold rounded-lg hover:bg-purple-500 hover:text-white transition-all duration-300"
            >
              <Users className="inline-block w-5 h-5 mr-2" />
              Join a Clan
            </Link>
          </div>
        </motion.div>
      </section>

      {/* Legal Notice */}
      <section className="py-8 text-center border-t border-gray-800">
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.8, delay: 1.4 }}
          className="text-sm text-gray-500"
        >
          <Shield className="inline-block w-4 h-4 mr-2" />
          <strong>Legal Notice:</strong> CineStox is a virtual trading platform for entertainment purposes only. 
          No real money is involved, and all trades are purely fictional. 
          This platform is designed to enhance fan engagement and is not a financial investment tool.
        </motion.div>
      </section>
    </div>
  );
};

export default HomePage; 