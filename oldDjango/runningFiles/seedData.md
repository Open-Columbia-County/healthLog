# 3 Users at least must be added before using the seed data see running.md file to know what users 2 and 3 should be

# Seed Data must be added in the order listed on this in order to work right

## #1 Enter into the healthApp_symptom table

INSERT INTO healthApp_symptom (symptom, info) VALUES
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

## #2 Enter into the healthApp_mediation table if on ADDINGPROVIDERACCESS BRANCH ONLY

INSERT INTO healthApp_medication (name, freq) VALUES
('Metformin', 'Daily'),
('Potassium', 'Daily'),
('Lantus', 'Daily'),
('NovoLog', 'Daily');

## #3 Enter into the healthApp_week table

INSERT INTO healthApp_week (title, writer_id) VALUES
('October 2-8', 2),
('October 2-8', 3);

## #4 Enter into the healthApp_log table

INSERT INTO healthApp_log (day, title, content, author_id, week_id) VALUES
('Tuesday', '10-4-22', 'Example User here having a good day', 2, 1),
('Tuesday', 'Busy day', 'This is just example content to show how the application works', 3, 2);

## #5 Enter into the healthApp_mood table

INSERT INTO healthApp_mood (tag, date, mood, log_id, symptom_id, user_id) VALUES
('Back pain', '2022-10-03 20:27:00.000000', 2, 1, 4, 2),
('Off ', '2022-10-04 05:50:00.000000', 1, 2, 11, 3),

## #6 Enter into the healthApp_sugar table

INSERT INTO healthApp_sugar (time, level, note_id, owner_id) VALUES
('2022-10-05 01:42:00.000000', 247, 2, 3),
('2022-10-05 03:39:00.000000', 76, 2, 3),
('2022-10-05 04:39:00.000000', 71, 2,3),

## #7 Enter into the healthApp_taken table if on ADDINGPROVIDERACCESS BRANCH ONLY

INSERT INTO healthApp_taken (when, day_id, dose, medication_id, member_id) VALUES
('2022-10-04 11:04:00.000000', 1, '20MEQ', 1, 1),
('2022-10-05 01:42:00.000000', 2, '35Units', 3, 3),
('2022-10-05 01:42:00.000000', 2, '10Units', 4, 3);
