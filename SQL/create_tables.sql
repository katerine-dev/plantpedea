CREATE TABLE plants (
	id INT AUTO_INCREMENT PRIMARY KEY,
	card_id INT NOT NULL,
	name TEXT,
	latin_name TEXT,
	solar_affinity TEXT,
	soil_type TEXT,
	woter_amout TEXT,
	days_to_collect INT
);

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email TEXT,
    password TEXT
);
