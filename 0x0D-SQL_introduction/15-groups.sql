-- number by score
SELECT score, COUNT(score) FROM second_table GROUP BY score DESC;