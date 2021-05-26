CREATE TABLE player (
	player_id	int PRIMARY KEY,
	player_name	varchar,
	position	varchar,
	dob date,
	height	int,
	weight	int,
	overall	int,
	potential_rating	int,
	best_position	varchar,
	best_overall_rating	int,
	value	int,
	wage	int,
	player_image_url	varchar,
	team_id	decimal(4,1),
	nationality	varchar
);

CREATE TABLE team(
	team_id	int PRIMARY KEY,
	team_name	varchar,
	league	varchar,
	overall	int,
	attack	int,
	midfield	int,
	defence	int,
	international_prestige	int,
	domestic_prestige	int,
	transfer_budget	int
);