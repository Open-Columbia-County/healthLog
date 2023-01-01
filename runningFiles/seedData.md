# 3 Users at least must be added before using the seed data see running.md file to know what users 2 and 3 should be

# Seed Data must be added in the order listed on this in order to work right

## #1 Enter into the healthApp_symptomlist table

INSERT INTO healthApp_symptomlist (symptom, info) VALUES
('General Headache', 'Non Migraine headache'),
('Migraine', 'General Migraine'),
('Fatigue', 'More than general fatigue'),
('General Back Pain', 'General aches and pains'),
('Chronic Back Pain', 'More than general aches and pains'),
('Depression', 'General Depression'),
('Anxiety', 'General Anxiety'),
('Panic Attack', 'Basic Panic Attack'),
('Fibromyalgia', 'General Fibromyalgia symptoms'),
('Aches and Pains', 'Just general aches and pains'),
('Other', 'Anything currently not listed');

## #2 Enter into the healthApp_mediation 

INSERT INTO healthApp_medication (name, freq, createdAt, updatedAt) VALUES
('Metformin', 'Daily', NOW(), NOW()),
('Potassium', 'Daily', NOW(), NOW()),
('Lantus', 'Daily', NOW(), NOW()),
('NovoLog', 'Daily', NOW(), NOW());

## #3 Enter into the healthApp_week table
Add manually



## #4 Enter into the healthApp_log table
Add manually



## #5 Enter into the healthApp_feeling table

INSERT INTO healthApp_feeling (date, feeling, content, createdAt, updatedAt, log_id, writer_id) VALUES 
(NOW(), 0, '', NOW(), NOW(), 1, 7), 
(NOW(), 3, '', NOW(), NOW(), 1, 7),
(NOW(), 4, '', NOW(), NOW(), 1, 8);

## #6 Enter into the healthApp_symptom table

INSERT INTO healthApp_symptom (date, content, createdAt, updatedAt, post_id, poster_id, symptom_id) VALUES 
(NOW(), '', NOW(), NOW(), 7,1,1),
(NOW(), '', NOW(), NOW(), 8,1,5),
(NOW(), '', NOW(), NOW(), 7,1,11);

## #7 Enter into the healthApp_sugar table

INSERT INTO healthApp_sugar (time, level, createdAt, updatedAt, entry_id, owner_id) VALUES 
(NOW(), 120, NOW(),NOW(), 7, 1),
(NOW(), 150, NOW(),NOW(), 9, 1),
(NOW(), 160, NOW(),NOW(), 7, 1);

## #8 Enter into the healthApp_taken 

INSERT INTO healthApp_taken (date, dose, createdAt, updatedAt, blog_id, medication_id, member_id) VALUES 
(NOW(), '', NOW(), NOW(), 7, 1, 1),
(NOW(), '', NOW(), NOW(), 7, 3, 1),
(NOW(), '', NOW(), NOW(), 9, 1, 1);


## #9 Seed data for Food (adjust person and record as needed)
INSERT INTO healthApp_food (food, calories, date, createdAt, updatedAt, person_id, record_id, meal) VALUES ('chips', '200', NOW(), NOW(), NOW(), 1, 7, 'Lunch'),('cereal', '400', NOW(), NOW(), NOW(), 1, 8, 'Breakfast'),('sandwich', '100', NOW(), NOW(), NOW(), 1, 7, 'Dinner');

## #10 Seed data for Sleep

INSERT INTO healthApp_sleep (date, sleep, wake, createdAt, updatedAt, journal_id, sleeper_id, content) VALUES 
(NOW(), NOW(), NOW(),NOW(), NOW(), 7, 1, ''),
(NOW(), NOW(), NOW(),NOW(), NOW(), 8, 1, ''),
(NOW(), NOW(), NOW(),NOW(), NOW(), 9, 1, '');