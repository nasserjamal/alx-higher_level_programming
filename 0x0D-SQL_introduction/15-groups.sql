-- Lists the number of records with the same score in the table second_table of the database hbtn_0c_0
SELECT score, COUNT(*) FROM second_table AS number GROUP BY number;
ORDER BY number DESC;
