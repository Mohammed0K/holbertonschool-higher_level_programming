-- script that creates a table second_table in the database
CREATE second_table(
  id INT,
  name VARCHAR(256),
  score INT
);

INSERT INTO second_table(id, name, score)VALUE(
  id = 1, name = "John", score = 10,
  id = 2, name = "Alex", score = 3,
  id = 3, name = “Bob”, score = 14,
  id = 4, name = “George”, score = 8
);
