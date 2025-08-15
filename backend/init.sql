-- CineStox Database Initialization
-- Sample data for Telugu movies and trading contracts

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Insert sample Telugu movies
INSERT INTO movies (
    id, title, telugu_title, language, status, genre,
    director, cast, star_actor, heroine, music_director,
    contract_symbol, initial_price, current_price, hype_score, reddit_sentiment,
    is_fdfs_event, is_festival_release, synopsis
) VALUES 
-- RRR (Released)
(
    uuid_generate_v4(), 'RRR', 'ఆర్‌ఆర్‌ఆర్', 'te', 'released',
    ARRAY['Action', 'Drama', 'Historical'], 
    ARRAY['S.S. Rajamouli'], 
    ARRAY['N.T. Rama Rao Jr.', 'Ram Charan', 'Alia Bhatt'],
    'N.T. Rama Rao Jr.', 'Alia Bhatt', 'M.M. Keeravani',
    'RRR', 100.0, 450.0, 95.0, 85.0,
    false, false,
    'A tale of two legendary revolutionaries and their journey far away from home.'
),

-- Pushpa: The Rise (Released)
(
    uuid_generate_v4(), 'Pushpa: The Rise', 'పుష్ప: ది రైజ్', 'te', 'released',
    ARRAY['Action', 'Crime', 'Drama'],
    ARRAY['Sukumar'],
    ARRAY['Allu Arjun', 'Rashmika Mandanna', 'Fahadh Faasil'],
    'Allu Arjun', 'Rashmika Mandanna', 'Devi Sri Prasad',
    'PUSHPA', 100.0, 320.0, 88.0, 78.0,
    false, false,
    'A laborer rises through the ranks of a red sandalwood smuggling syndicate.'
),

-- Salaar (In Production)
(
    uuid_generate_v4(), 'Salaar', 'సలార్', 'te', 'in_production',
    ARRAY['Action', 'Thriller'],
    ARRAY['Prashanth Neel'],
    ARRAY['Prabhas', 'Prithviraj Sukumaran', 'Shruti Haasan'],
    'Prabhas', 'Shruti Haasan', 'Ravi Basrur',
    'SALAAR', 100.0, 180.0, 92.0, 82.0,
    true, true,
    'A gang leader tries to keep a promise made to his dying friend.'
),

-- Guntur Kaaram (Post Production)
(
    uuid_generate_v4(), 'Guntur Kaaram', 'గుంటూర్ కారం', 'te', 'post_production',
    ARRAY['Action', 'Drama'],
    ARRAY['Trivikram Srinivas'],
    ARRAY['Mahesh Babu', 'Sreeleela', 'Meenakshi Chaudhary'],
    'Mahesh Babu', 'Sreeleela', 'Thaman S',
    'GUNTUR', 100.0, 140.0, 82.0, 72.0,
    true, true,
    'A story about a man who returns to his roots to solve family issues.'
),

-- Kalki 2898 AD (Post Production)
(
    uuid_generate_v4(), 'Kalki 2898 AD', 'కల్కి 2898 ఏడి', 'te', 'post_production',
    ARRAY['Sci-Fi', 'Action', 'Adventure'],
    ARRAY['Nag Ashwin'],
    ARRAY['Prabhas', 'Deepika Padukone', 'Amitabh Bachchan'],
    'Prabhas', 'Deepika Padukone', 'Santhosh Narayanan',
    'KALKI', 100.0, 200.0, 90.0, 80.0,
    true, false,
    'A futuristic sci-fi film set in the year 2898 AD.'
);

-- Update market data for released movies
UPDATE movies SET 
    current_price = 450.0,
    price_change_24h = 5.2,
    volume_24h = 1500000.0,
    market_cap = 450000000.0,
    high_24h = 460.0,
    low_24h = 440.0
WHERE contract_symbol = 'RRR';

UPDATE movies SET 
    current_price = 320.0,
    price_change_24h = -2.1,
    volume_24h = 980000.0,
    market_cap = 320000000.0,
    high_24h = 330.0,
    low_24h = 315.0
WHERE contract_symbol = 'PUSHPA';

UPDATE movies SET 
    current_price = 180.0,
    price_change_24h = 8.5,
    volume_24h = 750000.0,
    market_cap = 180000000.0,
    high_24h = 185.0,
    low_24h = 175.0
WHERE contract_symbol = 'SALAAR';

UPDATE movies SET 
    current_price = 140.0,
    price_change_24h = 6.7,
    volume_24h = 680000.0,
    market_cap = 140000000.0,
    high_24h = 142.0,
    low_24h = 138.0
WHERE contract_symbol = 'GUNTUR';

UPDATE movies SET 
    current_price = 200.0,
    price_change_24h = 7.8,
    volume_24h = 890000.0,
    market_cap = 200000000.0,
    high_24h = 205.0,
    low_24h = 198.0
WHERE contract_symbol = 'KALKI';

-- Set last price update timestamp
UPDATE movies SET last_price_update = NOW() WHERE contract_symbol IN ('RRR', 'PUSHPA', 'SALAAR', 'GUNTUR', 'KALKI');

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_movies_contract_symbol ON movies(contract_symbol);
CREATE INDEX IF NOT EXISTS idx_movies_language ON movies(language);
CREATE INDEX IF NOT EXISTS idx_movies_status ON movies(status);
CREATE INDEX IF NOT EXISTS idx_movies_hype_score ON movies(hype_score);
CREATE INDEX IF NOT EXISTS idx_movies_current_price ON movies(current_price);
CREATE INDEX IF NOT EXISTS idx_movies_volume_24h ON movies(volume_24h);
CREATE INDEX IF NOT EXISTS idx_movies_is_fdfs_event ON movies(is_fdfs_event);
CREATE INDEX IF NOT EXISTS idx_movies_is_festival_release ON movies(is_festival_release);

-- Insert sample users (for testing)
INSERT INTO users (
    id, email, username, hashed_password, first_name, last_name, telugu_name,
    preferred_language, current_balance, trading_score, research_score,
    is_verified, email_verified, is_active
) VALUES 
(
    uuid_generate_v4(), 'admin@cinestox.com', 'admin',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj/RK.s5u.Gi', -- password: admin123
    'Admin', 'User', 'అడ్మిన్ యూజర్', 'en', 100000.0, 2000, 500,
    true, true, true
),
(
    uuid_generate_v4(), 'telugu@cinestox.com', 'telugu_trader',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj/RK.s5u.Gi', -- password: admin123
    'Telugu', 'Trader', 'తెలుగు ట్రేడర్', 'te', 50000.0, 1500, 300,
    true, true, true
);

-- Create indexes for users
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_users_trading_score ON users(trading_score);
CREATE INDEX IF NOT EXISTS idx_users_preferred_language ON users(preferred_language);

-- Grant permissions
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO cinestox;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO cinestox;

-- Final statistics
SELECT 
    'Database initialization complete!' as status,
    COUNT(*) as total_movies,
    COUNT(CASE WHEN language = 'te' THEN 1 END) as telugu_movies,
    COUNT(CASE WHEN is_trading_active = true THEN 1 END) as active_contracts
FROM movies; 