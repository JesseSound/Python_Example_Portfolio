CREATE TABLE IF NOT EXISTS users (
	UserID text PRIMARY KEY,
	UserName text,
	MessagesSent integer DEFAULT 0,
	
	Warnings integer DEFAULT 0
);