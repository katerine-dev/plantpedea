CREATE TABLE plants (
	id UUID PRIMARY KEY DEFAULT(uuid()),
	card_id INT NOT NULL UNIQUE,
	name TEXT,
	latin_name TEXT,
	solar_affinity TEXT,
	soil_type TEXT,
	water_amout TEXT,
	days_to_collect TEXT
);

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email TEXT,
    password TEXT
);
